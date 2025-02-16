#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class DatabaseHandler(ABC):

    @abstractmethod
    def create():
        pass
    
    @abstractmethod
    def read():
        pass
    
    @abstractmethod
    def update():
        pass
    
    @abstractmethod
    def remove():
        pass
