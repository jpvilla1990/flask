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
        """
        response = requests.get(url)
        scrapped = BeautifulSoup(response.text, "html.parser")
        return scrapped

    def getPriceWollPlatz(self, scrapped):
        """
            Method to obtain the price from wollplatz website
        """
        productPrice = scrapped.findChild("span", {"class": "product-price"})
        priceNumber = productPrice.findAll("span", {"class": "product-price-amount"})[0].text
        currency = productPrice.findAll("span", {"class": "product-price-currency"})[0].text
        price = priceNumber + currency
        return dict({
                "price":price,
                })

    def getDeliveryTimeWollPlatz(self, scrapped):
        """
            Method to obtain the delivery time from wollplatz website
        """
        delivery_time_text = scrapped.find_all("div", {"id": "actie-bar-1"})[0].text.split("Lieferzeit")
        delivery_time = "Die Lieferzeit " + delivery_time_text[1]
        return dict({
                "deliveryTime":delivery_time,
                })

    def getSpecificationsFromTableWollPlatz(self, scrapped):
        """
            Method to obtain several sepcifications given in a table from woll platz
        """
        specifications_table = scrapped.findAll("div", {"id": "pdetailTableSpecs"})[0].findAll("td")
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