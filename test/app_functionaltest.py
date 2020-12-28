######################################################
# Unittest to check the methods of serviceFunctions  #
# Author: Juan Pablo Villa Serna                     #
######################################################
import os
import sys
import time
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

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestUnitTestApp(unittest.TestCase):

    """
        Class to perform several unittests
    """
    def test01_functional_testButton1(self):
        """
            TEST01: Checking if by pressing the html button, the corresponding file is generated
        """
        print("---------------------------------------------------------------")
        print("TEST01: Checking if by pressing the html button, the corresponding file is generated")
        print("---------------------------------------------------------------")
        chrome_options = Options()
        results_file = "../results/DMC-NaturaXL.csv"
        if os.path.exists(results_file):
            os.remove(results_file)
        path = os.path.abspath("../setup/chromedriver")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(path, options=chrome_options)
        driver.get("http://localhost:8050/")
        driver.set_window_size("1024", "768")
        button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "button1")))
        button.click()
        assert os.path.exists(results_file)
        driver.close()

    def test02_functional_testButton2(self):
        """
            TEST02: Checking if by pressing the html button, the corresponding file is generated
        """
        print("---------------------------------------------------------------")
        print("TEST02: Checking if by pressing the html button, the corresponding file is generated")
        print("---------------------------------------------------------------")
        chrome_options = Options()
        results_file = "../results/Drops-Safran.csv"
        if os.path.exists(results_file):
            os.remove(results_file)
        path = os.path.abspath("../setup/chromedriver")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(path, options=chrome_options)
        driver.get("http://localhost:8050/")
        driver.set_window_size("1024", "768")
        button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "button2")))
        button.click()
        assert os.path.exists(results_file)
        driver.close()

    def test03_functional_testButton3(self):
        """
            TEST03: Checking if by pressing the html button, the corresponding file is generated
        """
        print("---------------------------------------------------------------")
        print("TEST03: Checking if by pressing the html button, the corresponding file is generated")
        print("---------------------------------------------------------------")
        chrome_options = Options()
        results_file = "../results/Drops-BabyMerinoMix.csv"
        if os.path.exists(results_file):
            os.remove(results_file)
        path = os.path.abspath("../setup/chromedriver")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(path, options=chrome_options)
        driver.get("http://localhost:8050/")
        driver.set_window_size("1024", "768")
        button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "button3")))
        button.click()
        assert os.path.exists(results_file)
        driver.close()

    def test04_functional_testButton4(self):
        """
            TEST04: Checking if by pressing the html button, the corresponding file is generated
        """
        print("---------------------------------------------------------------")
        print("TEST04: Checking if by pressing the html button, the corresponding file is generated")
        print("---------------------------------------------------------------")
        chrome_options = Options()
        results_file = "../results/Stylecraft-SpecialDoubleKnit.csv"
        if os.path.exists(results_file):
            os.remove(results_file)
        path = os.path.abspath("../setup/chromedriver")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(path, options=chrome_options)
        driver.get("http://localhost:8050/")
        driver.set_window_size("1024", "768")
        button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "button4")))
        button.click()
        assert os.path.exists(results_file)
        driver.close()


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='unittest_app'),
        verbosity=2
    )
