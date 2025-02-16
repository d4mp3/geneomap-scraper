#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
from requests.models import Response

from network_client import NetworkClient

class MockResponse(Response):
    def __init__(self):
        self.status_code = 0
        self.headers = dict()
        self._content = True
        self._content_consumed = True
        self.raw = None


class TestNetworkClient(unittest.TestCase):
    __resp = None
    __client = None

    def setUp(self):
        self.__resp = MockResponse()
        self.__client = NetworkClient()
    
    def tearDown(self):
        del self.__resp
        del self.__client
        assert(self.__resp is None)
        assert(self.__client is None)

    @patch.object(NetworkClient, '_NetworkClient__get_response')
    def test__simple_get__good_response__return_html(self, mock_get_response):
        self.__resp.status_code = 200
        self.__resp.headers.update({'Content-Type': 'text/html; charset=UTF-8'})
        
        mock_get_response.return_value = self.__resp

        html = self.__client.simple_get("https://someurl.com")
        assert(html)

    @patch.object(NetworkClient, '_NetworkClient__get_response')
    def test__simple_get__status_code_404__return_none(self, mock_get_response):
        self.__resp.status_code = 404
        self.__resp.headers.update({'Content-Type': 'text/html; charset=UTF-8'})
        
        mock_get_response.return_value = self.__resp

        html = self.__client.simple_get("https://someurl.com")
        assert(html == None)

    @patch.object(NetworkClient, '_NetworkClient__get_response')
    def test__simple_get__content_type_wrong__return_none(self, mock_get_response):
        self.__resp.status_code = 200
        self.__resp.headers.update({'Content-Type': 'wrong'})
        
        mock_get_response.return_value = self.__resp

        html = self.__client.simple_get("https://someurl.com")
        assert(html == None)

    @patch.object(NetworkClient, '_NetworkClient__get_response')
    def test__simple_get__content_type_none__return_none(self, mock_get_response):
        self.__resp.status_code = 200
        self.__resp.headers.update({'Content-Type': None})
        
        mock_get_response.return_value = self.__resp

        html = self.__client.simple_get("https://someurl.com")
        assert(html == None)

if __name__ == '__main__':
    unittest.main()
