#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue
import threading

from custom_logger import CustomLogger
from typing import Callable, Any


class ThreadHandler():
    def __init__(self, num_of_threads=0, target=None): # type:ignore
        self.__queue = queue.Queue()
        self.__logger = CustomLogger()
        self.__num_of_threads = num_of_threads
        self.__target_func = target
        self.__stop_flag = True

    def add_jobs(self, jobs: Any) -> None:
        self.__logger.debug("Adding: {} jobs".format(len(jobs)))

        for item in jobs:
            self.__queue.put(item)

    def set_num_of_threads(self, num: int) -> None:
        self.__num_of_threads = num

    def set_target(self, func: Callable) -> None:
        self.__target_func = func

    def start(self) -> None:
        self.__stop_flag = False
        if self.__num_of_threads == 0:
            self.__logger.info(f'Calling Threadhandler::Start in the main thread')
            self.__worker()
        else:
            self.__logger.info(f'Calling Threadhandler::Start and spawning {self.__num_of_threads} threads')            
            for _ in range(self.__num_of_threads):
                threading.Thread(target=self.__worker, daemon=True).start()

            self.__queue.join()

    def stop(self) -> None:
        self.__logger.critical(f'Received stop request. Aborting...')
        self.__stop_flag = True
        while not self.__queue.empty():
            self.__queue.get()
            self.__queue.task_done()

    def __worker(self) -> None:
        thread_id = threading.get_native_id()
        self.__logger.info(f'Starting thread with id: {thread_id}')

        while not self.__stop_flag and not self.__queue.empty():
            job = self.__queue.get()
            self.__logger.debug(f'Working on job...')
            self.__target_func(job)
            self.__logger.info(f'Finished job. Jobs left in queue: {self.__queue.qsize()}')
            self.__queue.task_done()
        
        if self.__stop_flag:
            self.__logger.critical(f'Closing thread id: {thread_id}. Stop request received')
        else:
            self.__logger.info(f'Closing thread id: {thread_id}. Queue is empty')
