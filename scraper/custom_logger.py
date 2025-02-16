#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import os
import datetime
from typing import TypeVar, Type

class CustomFormatter(logging.Formatter):
    __grey = '\x1b[38;21m'
    __blue = '\x1b[38;5;39m'
    __yellow = '\x1b[38;5;226m'
    __red = '\x1b[38;5;196m'
    __bold_red = '\x1b[31;1m'
    __reset = '\x1b[0m'

    def __init__(self, fmt: str) -> None:
        super().__init__()
        self.FORMATS = {
            logging.DEBUG: self.__grey + fmt + self.__reset,
            logging.INFO: self.__blue + fmt + self.__reset,
            logging.WARNING: self.__yellow + fmt + self.__reset,
            logging.ERROR: self.__red + fmt + self.__reset,
            logging.CRITICAL: self.__bold_red + fmt + self.__reset
        }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


T = TypeVar('T', bound='CustomLogger')

class CustomLogger:
    __logger = None
    __stdout_handler = None
    __log_dir = './logs/'
    __log_level = logging.INFO
    __name = "scraper"
    __fmt = '%(asctime)s | %(threadName)s | %(levelname)8s | %(filename)s:%(lineno)d | %(message)s'

    def __new__(cls: Type[T], verbose : bool = False, file_output : bool = False): # type: ignore
        if cls.__logger is None:
            cls.__logger = logging.getLogger(cls.__name)
            
            #if(verbose):
            if (True): # TODO fix this
                    cls.__log_level = logging.DEBUG
            cls.__logger.setLevel(cls.__log_level)

            cls.__add_stream_handler(cls)
    
            if file_output:
                cls.__add_file_handler(cls, cls.__name, cls.__log_dir)

        return cls.__logger
    
    def __add_stream_handler(self: Type[T]) -> None: # type: ignore
        """Create stream handler for logging to stdout and set formatter"""

        self.__stdout_handler = logging.StreamHandler(sys.stdout)
        self.__stdout_handler.setLevel(self.__log_level)
        self.__stdout_handler.setFormatter(CustomFormatter(self.__fmt))
        self.__logger.addHandler(self.__stdout_handler)        

    def __add_file_handler(self: Type[T], name: str, log_dir: str) -> None: # type: ignore
        """Add a file handler for this logger with the specified `name` (and
        store the log file under `log_dir`)."""

        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
            except:
                print('{}: Cannot create directory {}. '.format(
                    self.__class__.__name__, log_dir),
                    end='', file=sys.stderr)
                log_dir = '/tmp' if sys.platform.startswith('linux') else '.'
                print(f'Defaulting to {log_dir}.', file=sys.stderr)

        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        log_name = f'{str(name).replace(" ", "_")}_{now}' 
        log_file = os.path.join(log_dir, log_name) + '.log'

        # Create file handler for logging to a file
        self.__logger.file_handler = logging.FileHandler(log_file) # type: ignore
        self.__logger.file_handler.setLevel(self.__log_level) # type: ignore
        self.__logger.file_handler.setFormatter(logging.Formatter(self.__fmt)) # type: ignore
        self.__logger.addHandler(self.__logger.file_handler) # type: ignore



    def debug(self, msg: str) -> None:
        self.__logger.debug(msg)

    def info(self, msg: str) -> None:
        self.__logger.info(msg)

    def warning(self, msg: str) -> None:
        self.__logger.warning(msg)

    def error(self, msg: str) -> None:
        self.__logger.error(msg)

    def critical(self, msg: str) -> None:
        self.__logger.critical(msg)