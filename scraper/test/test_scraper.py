#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
#add parent and current os paths
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


import unittest
from unittest.mock import patch
import selenium
from scraper import Scraper

#selenium.common.exceptions.StaleElementReferenceException


def inspect():
    import inspect
    #frame = inspect.currentframe()
    #frame.f_globals.update(frame.f_locals)
    #exec(inspect.getsource(my_function))
    #result = frame.f_globals['my_variable']

def save_to_database_mock(self, data_tuple: tuple) -> None:
    return

class TestScrapper(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    @patch.object(Scraper, '_Scraper__save_to_database')
    def test_get_table_data_Bolkow(self, mock):
        # Bolków
        batch = {
            "dolno\u015bl\u0105skie": {
                "parish_num": "66",
                "register_num": "74",
                "registers": {
                    "index.php?rid=5138&w=01ds&op=gt": {
                        "class": "B",
                        "title": "1833-34",
                        "text": "Bolk\u00f3w (ewang.)",
                        "entries_num": 433
                    }
                }
            }
        }

        first, last, num_of_threads = 0, 0, 0
        scraper = Scraper()
        scraper.run_scraper(batch, first, last, num_of_threads)

    @patch.object(Scraper, '_Scraper__save_to_database')
    def test_get_table_data_Chodecz(self, mock):
        # Chodecz
        batch = {
            "kujawsko-pomorskie": {
                "parish_num": "297",
                "register_num": "729",
                "registers": {
                    "index.php?rid=1260&w=02kp&op=gt": {
                        "class": "D",
                        "title": "1695,1700-04,28-61,63,65-1890",
                        "text": "Chodecz",
                        "entries_num": 26366
                    }
                }
            }
        }
        first, last, num_of_threads = 0, 0, 0
        scraper = Scraper()
        scraper.run_scraper(batch, first, last, num_of_threads)

    @patch.object(Scraper, '_Scraper__save_to_database')
    def test_get_table_data_Chelmica(self, mock):
        # Chełmica
        batch = {
            "kujawsko-pomorskie": {
                "parish_num": "297",
                "register_num": "729",
                "registers": {
                    "index.php?rid=4982&w=02kp&op=gt": {
                        "class": "D",
                        "title": "1761-88,1822-25,50-1920",
                        "text": "Che\u0142mica",
                        "entries_num": 5111
                    }
                }
            }
        }
        first, last, num_of_threads = 0, 0, 0
        scraper = Scraper()
        scraper.run_scraper(batch, first, last, num_of_threads)

    @patch.object(Scraper, '_Scraper__save_to_database')
    def test_get_table_data_Chelmonie(self, mock):
        # Chełmonie
        batch = {
            "kujawsko-pomorskie": {
                "parish_num": "297",
                "register_num": "729",
                "registers": {
                    "index.php?rid=6916&w=02kp&op=gt": {
                        "class": "D",
                        "title": "1749-58,61-1847",
                        "text": "Che\u0142monie",
                        "entries_num": 2464
                    }
                }
            }
        }
        first, last, num_of_threads = 0, 0, 0
        scraper = Scraper()
        scraper.run_scraper(batch, first, last, num_of_threads)

    @patch.object(Scraper, '_Scraper__save_to_database')
    def test_get_table_data_Warszawa_Wilanow(self, mock):
        # Warszawa-Wilanów
        # TODO check Wawrzyniec Kanabus
        batch = {
            "Warszawa": {
                "parish_num": "60",
                "register_num": "149",
                "registers": {
                    "index.php?rid=930&w=71wa&op=gt": {
                        "class": "D",
                        "title": "1757-1811,1835-37,78-82,1916-32,39-45",
                        "text": "Warszawa-Wilan\u00f3w \u015bw. Anna",
                        "entries_num": 5286
                    }
                }
            }
        }
        first, last, num_of_threads = 0, 0, 0
        scraper = Scraper()
        scraper.run_scraper(batch, first, last, num_of_threads)

    @patch.object(Scraper, '_Scraper__save_to_database')
    def test_get_table_data_Warszawa_Sluzew(self, mock):
        # Warszawa-Służew
        batch = {
            "Warszawa": {
                "parish_num": "60",
                "register_num": "149",
                "registers": {
                    "index.php?rid=1552&w=71wa&op=gt": {
                        "class": "D",
                        "title": "1711-23,94-1868,1880-84,1916-35",
                        "text": "Warszawa-S\u0142u\u017cew \u015bw. Katarzyna",
                        "entries_num": 13956
                    }
                }
            }
        }
        first, last, num_of_threads = 0, 0, 0
        scraper = Scraper()
        scraper.run_scraper(batch, first, last, num_of_threads)

    @patch.object(Scraper, '_Scraper__save_to_database')
    def test_get_table_data_Zoltance(self, mock):
        # Żółtańce Ukraina
        batch = {
            "Ukraina": {
                "parish_num": "60",
                "register_num": "149",
                "registers": {
                    "index.php?rid=11710&w=21uk&op=gt": {
                        "class": "D",
                        "title": "1776-89,91-99,1801-02,04-22,24-33,37-39,42,46-49,51-64",
                        "text": "\u017b\u00f3\u0142ta\u0144ce",
                        "entries_num": 1018
                    },
                }
            }
        }
        first, last, num_of_threads = 0, 0, 0
        scraper = Scraper()
        scraper.run_scraper(batch, first, last, num_of_threads)

    @patch.object(Scraper, '_Scraper__save_to_database')
    def test_get_table_data_Bialy_Kamien(self, mock):
        # Biały Kamień Ukraina
        batch = {
            "Ukraina": {
                "parish_num": "60",
                "register_num": "149",
                "registers": {
                    "index.php?rid=12213&w=21uk&op=gt": {
                        "class": "D",
                        "title": "1816-19,21-24,26-35",
                        "text": "Bia\u0142y Kamie\u0144",
                        "entries_num": 1012
                    }
                }
            }
        }
        first, last, num_of_threads = 0, 0, 0
        scraper = Scraper()
        scraper.run_scraper(batch, first, last, num_of_threads)


if __name__ == '__main__':
    unittest.main()