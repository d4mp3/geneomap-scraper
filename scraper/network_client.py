#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from requests.models import Response
from requests.exceptions import RequestException
from contextlib import closing
from custom_logger import CustomLogger

class NetworkClient():
    def __init__(self): # type:ignore
        self.__logger = CustomLogger(file_output=True)

    def simple_get(self, url: str) -> bytes | None:
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(self.__get_response(url)) as resp:
                self.__logger.info('Connecting to url: {}'.format(url))
                
                if self.__is_good_response(resp):
                    return resp.content
                else:
                    return None
    
        except RequestException as e:
            self.__logger.error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None
    
    def __get_response(self, url: str) -> Response | None:
        return get(url, stream=True)
    
    def __is_good_response(self, resp: Response) -> bool:
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type']
        return (resp.status_code == 200 
                and content_type is not None 
                and content_type.lower().find('html') > -1)
