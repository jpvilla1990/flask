######################################################
# Unittest to check the methods of serviceFunctions  #
# Author: Juan Pablo Villa Serna                     #
######################################################
import os
import sys
app_path = "../"
sys.path.append(app_path)

from tools.routeFunctions import RouteFunctions
from tools.serviceFunctions import ServiceFunctions

import unittest
import mock
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xmlrunner
from mock import MagicMock

class TestUnitTestApp(unittest.TestCase):

    """
        Class to perform several unittests
    """
    #@mock.patch('tools.routeFunctions.RouteFunctions.serviceFunctions.scrapeData')
    @mock.patch('tools.serviceFunctions.ServiceFunctions.scrapeData')
    def test01_functional_testButton(self, scrapeData):
        """
            TEST01: Checking method scrapeData from ServiceFunctions
        """
        print("---------------------------------------------------------------")
        print("TEST01: Checking if by pressing the html button, the corresponding url is scrapped")
        print("---------------------------------------------------------------")
        chrome_options = Options()
        path = os.path.abspath("../setup/chromedriver")
        #chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("user-data-dir=/home/jpvilla1990")
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(path, options=chrome_options)
        driver.get("http://http://localhost:8050/")
        button = driver.find_element_by_id('button1')
        button.click()
        assert scrapeData.called
        driver.close()

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='unittest_app'),
        verbosity=2
    )