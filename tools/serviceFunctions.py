# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

class ServiceFunctions(object):
    """
        Class to simplify functions for every route
    """
    def printString(self, valueToPrint):
        """
            Method to handle a button via POST
        """
        print(valueToPrint)

    def scrapeData(self, url):
        """
            Method to scrape an URL
            @url string with url to scrape

            return a bs4 object with the scraped website
        """
        response = requests.get(url)
        scraped = BeautifulSoup(response.text, "html.parser")
        return scraped

    def getPriceWollPlatz(self, scraped):
        """
            Method to obtain the price from wollplatz website
            @scraped bs4 object with scraped website

            return dict with price
        """
        productPrice = scraped.findChild("span", {"class": "product-price"})
        priceNumber = productPrice.findAll("span", {"class": "product-price-amount"})[0].text
        currency = productPrice.findAll("span", {"class": "product-price-currency"})[0].text
        price = priceNumber + currency
        return dict({
                "price":price,
                })

    def getDeliveryTimeWollPlatz(self, scraped):
        """
            Method to obtain the delivery time from wollplatz website
            @scraped bs4 object with scraped website

            return dict with delivery time
        """
        delivery_time_text = scraped.find_all("div", {"id": "actie-bar-1"})[0].text.split("Lieferzeit")
        delivery_time = "Die Lieferzeit " + delivery_time_text[1]
        return dict({
                "deliveryTime":delivery_time,
                })

    def getSpecificationsFromTableWollPlatz(self, scraped):
        """
            Method to obtain several sepcifications given in a table from woll platz
            @scraped bs4 object with scraped website

            return dict with needle size and composition
        """
        specifications_table = scraped.findAll("div", {"id": "pdetailTableSpecs"})[0].findAll("td")
        i=0
        needleSize = None
        composition = None
        for element in specifications_table:
            if "Nadelstärke" in element.text:
                needleSize = specifications_table[i + 1].text
            elif "Zusammenstellung" in element.text:
                composition = specifications_table[i + 1].text
            i = i + 1

        return dict({
                "needleSize":needleSize,
                "composition":composition,
                })