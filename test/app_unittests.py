######################################################
# Unittest to check the methods of serviceFunctions  #
# Author: Juan Pablo Villa Serna                     #
######################################################

import sys
app_path = "../"
sys.path.append(app_path)

from tools.routeFunctions import RouteFunctions
from tools.serviceFunctions import ServiceFunctions

from flask import Flask, render_template, request

import unittest
import mock
import xmlrunner
from mock import MagicMock

class TestUnitTestApp(unittest.TestCase):

    """
        Class to perform several unittests
    """

    @mock.patch('tools.serviceFunctions.requests.get')
    @mock.patch('tools.serviceFunctions.BeautifulSoup')
    def test01_serviceFunctions_scrapeData(self, beautifulSoup, requestsGet):
        """
            TEST01: Checking method scrapeData from ServiceFunctions
        """
        print("---------------------------------------------------------------")
        print("TEST01: Checking method scrapeData from ServiceFunctions")
        print("---------------------------------------------------------------")
        service = ServiceFunctions()
        url = "xxx"
        service.scrapeData(url)
        requestsGet.assert_any_call(url)
        assert beautifulSoup.called

    @mock.patch('tools.serviceFunctions.BeautifulSoup')
    def test02_serviceFunctions_getPriceWollPlatz(self, beautifulSoup):
        """
            TEST02: Checking method getPriceWollPlatz from ServiceFunctions
        """
        print("---------------------------------------------------------------")
        print("TEST02: Checking method getPriceWollPlatz from ServiceFunctions")
        print("---------------------------------------------------------------")
        service = ServiceFunctions()
        beautifulSoup.findChild = MagicMock(name='findChild')
        service.getPriceWollPlatz(beautifulSoup)
        beautifulSoup.findChild.assert_any_call("span", {"class": "product-price"})
        
    @mock.patch('tools.serviceFunctions.BeautifulSoup')
    def test03_serviceFunctions_getDeliveryTimeWollPlatz(self, beautifulSoup):
        """
            TEST03: Checking method getDeliveryTimeWollPlatz from ServiceFunctions
        """
        print("---------------------------------------------------------------")
        print("TEST03: Checking method getDeliveryTimeWollPlatz from ServiceFunctions")
        print("---------------------------------------------------------------")
        service = ServiceFunctions()
        beautifulSoup.find_all = MagicMock(name='find_all')
        service.getDeliveryTimeWollPlatz(beautifulSoup)
        beautifulSoup.find_all.assert_any_call("div", {"id": "actie-bar-1"})
        
    @mock.patch('tools.serviceFunctions.BeautifulSoup')
    def test04_serviceFunctions_getSpecificationsFromTableWollPlatz(self, beautifulSoup):
        """
            TEST04: Checking method getSpecificationsFromTableWollPlatz from ServiceFunctions
        """
        print("---------------------------------------------------------------")
        print("TEST04: Checking method getSpecificationsFromTableWollPlatz from ServiceFunctions")
        print("---------------------------------------------------------------")
        service = ServiceFunctions()
        beautifulSoup.findAll = MagicMock(name='findAll')
        service.getSpecificationsFromTableWollPlatz(beautifulSoup)
        beautifulSoup.findAll.assert_any_call("div", {"id": "pdetailTableSpecs"})

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='unittest_results'),
        verbosity=2
    )