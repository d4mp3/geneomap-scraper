#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error
from custom_logger import CustomLogger
from collections import OrderedDict

DUMMY_DATA = [OrderedDict([('_id', '1834_428_B_Bolków (ewang.)'), ('year', '1834'), ('year_info', None), ('act', None),
                           ('act_info', None), ('name', 'Paulina Luiza'), ('name_info', None), ('surname', 'Heilmann'),
                           ('suname_info', None), ('father', 'Karol Fryderyk'), ('father_info', None), ('mother', 'Krystyna Eleonora'),
                           ('mother_info', None), ('mother_surname', 'Tschiersich'), ('mother_surname_info', None),
                           ('parish', 'Bolków (ewang.)'), ('parish_info', None), ('place', 'Bolków'), ('place_info', None),
                           ('notes', 'Uwagi: karta 86,'), ('url', 'https://geneteka.genealodzy.pl/index.php?rid=5138&w=01ds&op=gt')]),
              OrderedDict([('_id', '1834_429_B_Bolków (ewang.)'), ('year', '1834'), ('year_info', None), ('act', None),
                           ('act_info', None), ('name', 'Paweł Rudolf'), ('name_info', None), ('surname', 'Länder'), ('suname_info', None),
                           ('father', 'Gotlib Ludwik'), ('father_info', None), ('mother', 'Fryderyka Emilia'), ('mother_info', None),
                           ('mother_surname', 'Pathe'), ('mother_surname_info', None), ('parish', 'Bolków (ewang.)'), ('parish_info', None),
                           ('place', 'Bolków'), ('place_info', None), ('notes', 'Uwagi: karta 100,'), ('url', 'https://geneteka.genealodzy.pl/index.php?rid=5138&w=01ds&op=gt')]),
              OrderedDict([('_id', '1834_430_B_Bolków (ewang.)'), ('year', '1834'), ('year_info', None), ('act', None), ('act_info', None),
                           ('name', 'Rozyna Karolina'), ('name_info', None), ('surname', 'Pohl'), ('suname_info', None),
                           ('father', 'Jan Karol'), ('father_info', None), ('mother', 'Joanna Henrietta'), ('mother_info', None),
                           ('mother_surname', 'Kliem'), ('mother_surname_info', None), ('parish', 'Bolków (ewang.)'), ('parish_info', None),
                           ('place', 'Wolbromek'), ('place_info', None), ('notes', 'Uwagi: karta 99,'), ('url', 'https://geneteka.genealodzy.pl/index.php?rid=5138&w=01ds&op=gt')]),
              OrderedDict([('_id', '1834_431_B_Bolków (ewang.)'), ('year', '1834'), ('year_info', None), ('act', None), ('act_info', None),
                           ('name', 'Wilhelmina Albertyna Ernestyna'), ('name_info', None), ('surname', 'Kirsch'), ('suname_info', None),
                           ('father', 'Jan Karol Franciszek'), ('father_info', None), ('mother', 'Joanna Eleonora'), ('mother_info', None),
                           ('mother_surname', 'Hohberg'), ('mother_surname_info', None), ('parish', 'Bolków (ewang.)'), ('parish_info', None),
                           ('place', 'Bolków'), ('place_info', None), ('notes', 'Uwagi: karta 158,'), ('url', 'https://geneteka.genealodzy.pl/index.php?rid=5138&w=01ds&op=gt')]),
              OrderedDict([('_id', '1834_432_B_Bolków (ewang.)'), ('year', '1834'), ('year_info', None), ('act', None), ('act_info', None),
                           ('name', 'Wilhelmina Augusta'), ('name_info', None), ('surname', 'Schrodt'), ('suname_info', None),
                           ('father', 'Karol'), ('father_info', None), ('mother', 'Maria Rozyna'), ('mother_info', None),
                           ('mother_surname', 'Blümel'), ('mother_surname_info', None), ('parish', 'Bolków (ewang.)'), ('parish_info', None),
                           ('place', 'Bolków'), ('place_info', None), ('notes', 'Uwagi: karta 130,'), ('url', 'https://geneteka.genealodzy.pl/index.php?rid=5138&w=01ds&op=gt')])]



class SqlHandler():

    def __init__(self):
        self.db = None
        self.con = None
        self.cur = None
        self.params = None
        self.logger = CustomLogger()


    def connect(self, db_name: str) -> None:
        try:
            self.con = sqlite3.connect(db_name)
            self.cur = self.con.cursor()
        except Error as e:
            print(e)


    def create_table(self, table_name: str, *args):
        entries, = args

        for count, entry in enumerate(entries):
            entry["_id UNIQUE"] = entry["_id"]
            del entry["_id"]

        columns = ', '.join(list(args[0][0].keys()))
        print(columns)
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")


    def insert(self, table_name, *args):
        params = tuple(args[0][0].keys())
        records, = list(args)
        question_marks = ','.join(['?'] * len(params))

        for record in records:
            values = tuple(record.values())
            self.cur.execute(f"INSERT OR IGNORE INTO {table_name} VALUES ({question_marks})", values)
            self.con.commit()


    def select_one(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    def drop_table(self):
        pass


if __name__ == '__main__':
    sql_handler = SqlHandler()
    sql_handler.connect("../data/sqlite.db")
    sql_handler.create_table('deaths', DUMMY_DATA)
    sql_handler.insert('deaths', DUMMY_DATA)