#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import itertools
from custom_logger import CustomLogger
from typing import Iterable

class MongodbHandler():

    def __init__(self): # type:ignore
        self.client = MongoClient()
        self.con = None
        self.db = None
        self.logger = CustomLogger()


    def connect(self, host_name: str='localhost', port: int=27017) -> None:
        self.con = MongoClient()
        self.__get_database()
        self.logger.info(f'Connected to {host_name}:{port}')

    def __get_database(self) -> None:
        self.db = self.client.geneomap_db

    def create_table(self, table_name: str, *args: str) -> None:
        self.collection = self.db[table_name]
        self.logger.debug(f'Created table {table_name}')

    def insert(self, *args: Iterable, table_name: str, unique_id: str=None) -> None:
        self.logger.debug(f'Inserting into {table_name}')
        merged = list(itertools.chain(*args))    

        post_ids = self.db[table_name].insert_many(merged).inserted_ids

    def select_one(self, data: dict, collection: str | None = None) -> dict | None:
        # find in all collections
        if collection is None:
            found = None
            for col in self.db.list_collection_names():
                found = self.db[col].find_one(data)
                if found:
                    return found
            return found
        # find in collections in list
        elif isinstance(collection, list):
            found = None
            for col in collection:
                found = found + self.db[col].find_one(data)
            return found
        # find in specified collection
        else:
            return self.db[collection].find_one(data)

    def find_all_uniques(self, key: str, collection: str | list | None = None) -> list | None:
        # find in all collections
        if collection is None:
            found: list = []
            for col in self.db.list_collection_names():
                found = found + self.db[col].distinct(key)
            return found
        # find in collections in list
        elif isinstance(collection, list):
            found = []
            for col in collection:
                found = found + self.db[col].distinct(key)
            return found
        # find in specified collection
        else:
            return self.db[collection].distinct(key)

    def update(self) -> None:
        pass
    
    def remove(self) -> None:
        pass
    