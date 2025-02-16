#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json


from pymongo.errors import ServerSelectionTimeoutError, BulkWriteError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, TimeoutException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

from time import sleep

from collections import OrderedDict
from typing import TypeVar

from custom_logger import CustomLogger
from thread_handler import ThreadHandler
from mongodb_handler import MongodbHandler


DEFAULT_FILE_PATH = './data/batch_links.json'
DEFAULT_NUM_OF_THREADS = 0
options = webdriver.ChromeOptions()
options.headless = True

# type annotations
WebdriverType = TypeVar('WebdriverType', bound=webdriver.chrome.webdriver.WebDriver)

# define Python user-defined exceptions
class EntriesNumZeroException(Exception):
    "Raised when the entries_num defined in batch links is 0"
    pass

class InvalidSubpagesNumException(Exception):
    "Raised when the subpage number is invalid"
    pass

class Scraper:
    def __init__(self): # type:ignore
        self.batch_num = 0
        self.logger = CustomLogger(verbose=True, file_output=True)
        self.thread_handler = ThreadHandler()
        self.database_handler = MongodbHandler()
        self.database_handler.connect()
        self.database_handler.create_table('births')
        self.database_handler.create_table('marriages')
        self.database_handler.create_table('deaths')

    def run_scraper(self, batches: dict, first: int, last: int, num_of_threads: int) -> None:
        self.logger.info("===================================================================")
        self.logger.info("Running scrapper with parameters: first batch: {}, last batch: {}, num of threads: {})".format(
            first, last, num_of_threads))

        # prepare jobs batch
        jobs = []
        for province in batches.keys():
            for i, reg in enumerate(batches[province]['registers'].keys()):
                jobs.append({reg: batches[province]['registers'][reg]})

        jobs = jobs[first: (last+1)]  # get a slice
        self.logger.debug("Number of jobs: {}".format(len(jobs)))
        self.batch_num = len(jobs)

        # set up thread handler and start it
        self.thread_handler.add_jobs(jobs)
        self.thread_handler.set_num_of_threads(num_of_threads)
        self.thread_handler.set_target(self.__try_get_table_data)
        self.thread_handler.start()  # this function will block main thread

    def __save_to_database(self, data_tuple: tuple) -> None:
        table_name, data = data_tuple
        self.database_handler.insert(data, table_name=table_name)

        url = data[0]['url']
        self.database_handler.insert([{'_id': url}], table_name='url_ids')

    def __is_item_in_db(self, url: str) -> dict | None:
        return self.database_handler.select_one({"_id": url}, collection='url_ids')

    def __try_get_table_data(self, item: dict) -> None:
        driver = None
        url = list(item)[0]
        try:
            if self.__is_item_in_db(url):
                self.logger.warning(f"Url: {url} already found in database. Ignoring...")
            else:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                data_tuple = self.__get_table_data(driver, item)
                self.__save_to_database(data_tuple)
        except EntriesNumZeroException as e:
            self.logger.error("EntriesNumZeroException")
            self.logger.error("Found a batch with entries num set to 0. Skipping...")
        except InvalidSubpagesNumException as e:
            self.logger.error("InvalidSubpagesNumException")
            self.logger.error("Found a batch with invalid subpages num. Skipping...")
        except StaleElementReferenceException as e:
            self.logger.error("StaleElementReferenceException")
            self.logger.error(e, stack_info=True)
            self.logger.error("Putting failed job back into queue...")
            self.thread_handler.add_jobs([item])
        except TimeoutException as e:
            self.logger.error("TimeoutException")
            self.logger.error(e, stack_info=True)
            self.logger.error("Putting failed job back into queue...")
            self.thread_handler.add_jobs([item])
        except WebDriverException as e:
            self.logger.error("WebDriverException")
            self.logger.error(e, stack_info=True)
            self.logger.error("Putting failed job back into queue...")
            self.thread_handler.add_jobs([item])
        except BulkWriteError as e:
            self.logger.warning("BulkWriteError occured. Ignoring...")
            self.logger.warning(e)
        except ServerSelectionTimeoutError as e:
            self.logger.critical("Exception while connecting to database")
            self.logger.error(e, stack_info=True)
            self.thread_handler.stop()
            raise e
        except OSError as e:
            self.logger.critical("OSError occured. Retrying...")
            self.logger.error(e, stack_info=True)
            self.thread_handler.add_jobs([item])
        except EOFError as e:
            self.logger.critical("EOFError occured. Retrying...")
            self.logger.error(e, stack_info=True)
            self.logger.error("Putting failed job back into queue...")
            self.thread_handler.add_jobs([item])
        except TypeError as e:
            self.logger.error("TypeError occurred. Ignoring bad data... ", type(e).__name__)
            self.logger.error(e, stack_info=True)
            self.logger.critical("Bad url: ", url)
        except Exception as e:
            self.logger.critical("Exception not handled yet! ", type(e).__name__)
            self.logger.critical(e, stack_info=True)
            self.thread_handler.stop()
            raise e
        finally:
            if driver:
                driver.quit()

    def __get_table_data(self, driver: WebdriverType, input_dict: dict) -> tuple:
        short_url = list(input_dict)[0]
        expected_entries_num = input_dict[short_url]['entries_num']
        if expected_entries_num == 0:
            raise EntriesNumZeroException

        url = 'https://geneteka.genealodzy.pl/' + list(input_dict)[0] + \
              "&ordertable=[[9,\"asc\"]]&searchtable=&rpp1=0&rpp2=50"
        self.logger.info(f'Processing batch url: {url}')
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "dataTables_info")))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.tablesearch'))
        )

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        content_class = soup.find("div", {"class": "dataTables_info"})['id']
        paginate_buttons = soup.find_all("div", "dataTables_paginate paging_simple_numbers")

        subpages_num = 0
        try:
            subpages_num = int(paginate_buttons[0].find_all('a')[-2].text)
        except ValueError:
            raise InvalidSubpagesNumException

        all_single_events = []
        total_num = 0
        skipped_num = 0
        for i in range(subpages_num):
            cur_url = driver.current_url
            self.logger.debug("Reading subpage: {}, url: {}".format(i+1, cur_url))
            driver.get(cur_url)

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "dataTables_info")))
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.tablesearch'))
            )

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            table_rows = soup.find_all('tr', {'class': ['odd', 'even']})

            for row in table_rows:
                single_event = []
                for td in row.find_all('td'):

                    # Get text and img info and replace empty strings with None
                    text = td.text.strip() if td.text else None
                    info = None
                    if td.img:
                        info = td.img.get('title').strip().strip('\r')

                    single_event.append(text)
                    single_event.append(info)

                # Check for duplicates in already scrapped events and skip them
                total_num = total_num + 1
                if single_event in all_single_events:
                    self.logger.error("Duplicate found: {}".format(single_event))
                    skipped_num = skipped_num + 1
                else:
                    all_single_events.append(single_event)

            # Retry clicking on StaleElementReferenceException
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'paginate_button.next'))).click()
                sleep(1)
            except StaleElementReferenceException as e:
                self.logger.error("Stale element exception. Retrying...")
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'paginate_button.next'))).click()
                sleep(1)

        table2function = {
            'table_d_info': self.__get_deaths,
            'table_b_info': self.__get_births,
            'table_s_info': self.__get_marriages
        }
        data_tuple = table2function[content_class](all_single_events, short_url)
        self.logger.info("Expected events: {}".format(expected_entries_num))
        self.logger.info("All events found: {}".format(total_num))
        self.logger.info("all_single_events found: {}".format(len(all_single_events)))
        self.logger.info("Events skipped: {}".format(skipped_num))
        return data_tuple

    def __get_deaths(self, events: list, url: str) -> tuple:
        self.logger.info('Calling __get_deaths')
        url_id = url.split('rid=')[-1].split('&')[0]
        deaths = []
        for index, event in enumerate(events):
            event_id = '_'.join([url_id, 'D', str(index), event[0], event[14]])

            deaths.append(OrderedDict({
                '_id': event_id,
                'year': event[0],
                'year_info': event[1],
                'act': event[2],
                'act_info': event[3],
                'name': event[4],
                'name_info': event[5],
                'surname': event[6],
                'surname_info': event[7],
                'father': event[8],
                'father_info': event[9],
                'mother': event[10],
                'mother_info': event[11],
                'mother_surname': event[12],
                'mother_surname_info': event[13],
                'parish': event[14],
                'parish_info': event[15],
                'place': event[16],
                'place_info': event[17],
                'notes': event[19],
                'url': url
                }))
        
        return ('deaths', deaths)


    def __get_births(self, events: list, url: str) -> tuple:
        self.logger.info('Calling __get_births')
        url_id = url.split('rid=')[-1].split('&')[0]
        births = []

        for index, event in enumerate(events):
            event_id = '_'.join([url_id, 'B', str(index), event[0], event[14]])

            births.append(OrderedDict({
                '_id': event_id,
                'year': event[0],
                'year_info': event[1],
                'act': event[2],
                'act_info': event[3],
                'name': event[4],
                'name_info': event[5],
                'surname': event[6],
                'surname_info':  event[7],
                'father': event[8],
                'father_info': event[9],
                'mother': event[10],
                'mother_info': event[11],
                'mother_surname': event[12],
                'mother_surname_info': event[13],
                'parish': event[14],
                'parish_info': event[15],
                'place': event[16],
                'place_info': event[17],
                'notes': event[19],
                'url': url
                }))

        return ('births', births)

    def __get_marriages(self, events: list, url: str) -> tuple:
        self.logger.info('Calling __get_marriages')
        url_id = url.split('rid=')[-1].split('&')[0]
        marriages = []

        for index, event in enumerate(events):
            event_id = '_'.join([url_id, 'M', str(index), event[0], event[16]])

            marriages.append(OrderedDict({
                '_id': event_id,
                'year': event[0],
                'year_info': event[1],
                'act': event[2],
                'act_info': event[3],
                'male_name': event[4],
                'male_name_info': event[5],
                'male_surname': event[6],
                'male_surname_info': event[7],
                'male_parents': event[8],
                'male_parents_info': event[9],
                'female_name': event[10],
                'female_name_info': event[11],
                'female_surname': event[12],
                'female_surname_info': event[13],
                'female_parents': event[14],
                'female_parents_info': event[15],
                'parish': event[16],
                'parish_info': event[17],
                'notes': event[19],
                'url': url
                }))

        return ('marriages', marriages)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Scrapper for geneo data')
    parser.add_argument('-f', '--file', action='store', help='Filename to read data. \
                        Default path: ./data/batch_links.json')
    parser.add_argument('--first', action='store', type=int, help='Index of the first batch to be scrapped')
    parser.add_argument('--last', action='store', type=int, help='Index of the last batch to be scrapped')
    parser.add_argument('-n', '--num_of_threads', action='store', type=int, help='Number of threads to spawn (default: 0)')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='Increase logging output with debug messages')
    parser.add_argument('-l', '--log_to_file', action='store_true', default=False, help='Log to file in /logs/')

    args = parser.parse_args()

    if args.first is None or args.last is None:
        raise argparse.ArgumentError(args.first, message="Error: --first and --last parameters are required")

    first = args.first
    last = args.last
    filepath = args.file if args.file else DEFAULT_FILE_PATH
    num_of_threads = args.num_of_threads if args.num_of_threads else DEFAULT_NUM_OF_THREADS
    batches: dict[str, dict]

    logger = CustomLogger(verbose=args.verbose, file_output=args.log_to_file)

    logger.debug("Reading from filepath: {}".format(filepath))

    with open(filepath, 'r') as f:
        batches = json.load(f, object_pairs_hook=dict)

    scrapper = Scraper()
    scrapper.run_scraper(batches, first, last, num_of_threads)
