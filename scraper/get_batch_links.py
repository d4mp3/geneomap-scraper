#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import argparse
import json
from custom_logger import CustomLogger
from network_client import NetworkClient
import os
from collections import OrderedDict
import requests


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


START_SITE = "https://geneteka.genealodzy.pl/rejestry.php?lang=pol"
DEFAULT_FILE_PATH = './data/batch_links.json'

logger = CustomLogger()
client = NetworkClient()
options = webdriver.ChromeOptions()
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
def get_batch_links(url: str) -> OrderedDict:

    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.html.body.center.table
    tr = soup.find_all('tr')[4:] # check if all are inside
    entry = tr[0].td.table.tr
    td = entry.find_all('td')[5:]

    batch_links: OrderedDict = OrderedDict()
    # iterate over provinces
    for i in range(0, len(td), 4):
        province = td[i].text.strip()
        parish_num = td[i+1].text.strip()
        register_num = td[i+2].text.strip()
        registers = td[i+3].find_all('a')

        province_dict = OrderedDict()
        register_dict = OrderedDict()

        # iterate over registers in one province
        for item in registers:
            href = item['href']
            title = item['title'],
            text = item.text

            register_dict.update({
                href: {
                    'class': item['class'][0],
                    'title': item['title'],
                    'text': item.text
                }
            })
            #print ('register_dict keys: ', len(register_dict.keys()))

        province_dict.update({
            province: {
                'parish_num': parish_num,
                'register_num': register_num,
                'registers': register_dict
            }
        })
        #print('province_dict keys: ', len(province_dict.keys()))

        batch_links.update(province_dict)
        #print('batch_links keys: ', len(batch_links.keys()))

        logger.info(f"Found {register_num} batches in total for: {province}")

    return batch_links

def get_register_data(batch_dict: OrderedDict) -> OrderedDict:

    for province in batch_dict.keys():
        registers = batch_dict[province]['register_num']
        parishes = batch_dict[province]['parish_num']
        logger.info(f"Processing key: {province}. Parish num: {parishes} Registers num: {registers}")

        options.headless = True
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        count = len(batch_dict[province]['registers'].keys())
        for i, reg in enumerate(batch_dict[province]['registers'].keys()):
            url = 'https://geneteka.genealodzy.pl/' + reg
            logger.info(f"Url: {url}   {i}/{count}")
            driver.get(url)
            try:
                WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "dataTables_info")))
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                element = soup.find("div", {"class": "dataTables_info"})

                entries_num = element.text.replace(',', '')
                batch_dict[province]['registers'][reg]['entries_num'] = entries_num
            except TimeoutException as e:
                logger.critical("Timed out. Setting entries num to None")
                entries_num = None
                batch_dict[province]['registers'][reg]['entries_num'] = entries_num

    return batch_dict



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for getting batch links for future processing')
    parser.add_argument('-f', '--file', action='store', help='Filename to save data. \
                        Default path: ./data/batch_links.json')

    args = parser.parse_args()

    batch_list = get_batch_links(START_SITE)
    batch_list = get_register_data(batch_list)

    filepath = args.file if args.file else DEFAULT_FILE_PATH

    if not os.path.exists('./data'):
        os.makedirs('./data')

    if os.path.isfile(filepath):
        with open(filepath, 'w') as f:
            json.dump(batch_list, f)
    else:
        with open(filepath, 'a') as f:
            json.dump(batch_list, f)

    logger.info("Data saved to filepath: {}".format(filepath))
