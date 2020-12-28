# -*- coding: utf-8 -*-
from flask import render_template
from tools.serviceFunctions import ServiceFunctions
import numpy as np

class RouteFunctions(object):
    """
        Class to simplify functions for every route
    """
    def __init__(self):
        self.serviceFunctions = ServiceFunctions()

    def paramsSaveCsv(self, name, dictionary):
        """
            Method to save csv file
        """
        csv_file = name + ".csv"
        columns = list(dictionary.keys())
        params = list(dictionary.values())
        npParams = np.array([columns,params])
        np.savetxt("results/" + name + ".csv", npParams, fmt="%s", delimiter=";")

    def ButtonRequestHome(self, requestObject, buttons, render, urls):
        """
            Method to handle a button via POST
            if nothing is executed the function returns false
        """
        params = dict()
        if requestObject.method == 'POST':
            if requestObject.form.get(buttons[0]) == buttons[0]:
                scraped = self.serviceFunctions.scrapeData(urls[0])
                price = self.serviceFunctions.getPriceWollPlatz(scraped)
                deliveryTime = self.serviceFunctions.getDeliveryTimeWollPlatz(scraped)
                table = self.serviceFunctions.getSpecificationsFromTableWollPlatz(scraped)
                params.update(price)
                params.update(deliveryTime)
                params.update(table)
                self.paramsSaveCsv(buttons[0], params)
                return render_template(render,
                             button1=buttons[0],
                             button2=buttons[1],
                             button3=buttons[2],
                             button4=buttons[3],
                             buttonTag=True,
                             url=urls[0],
                             price=params["price"],
                             deliveryTime=params["deliveryTime"],
                             needleSize=params["needleSize"],
                             composition=params["composition"],
                             )
            elif requestObject.form.get(buttons[1]) == buttons[1]:
                scraped = self.serviceFunctions.scrapeData(urls[1])
                price = self.serviceFunctions.getPriceWollPlatz(scraped)
                deliveryTime = self.serviceFunctions.getDeliveryTimeWollPlatz(scraped)
                table = self.serviceFunctions.getSpecificationsFromTableWollPlatz(scraped)
                params.update(price)
                params.update(deliveryTime)
                params.update(table)
                self.paramsSaveCsv(buttons[1], params)
                return render_template(render,
                             button1=buttons[0],
                             button2=buttons[1],
                             button3=buttons[2],
                             button4=buttons[3],
                             buttonTag=True,
                             url=urls[1],
                             price=params["price"],
                             deliveryTime=params["deliveryTime"],
                             needleSize=params["needleSize"],
                             composition=params["composition"],
                             )
            elif requestObject.form.get(buttons[2]) == buttons[2]:
                scraped = self.serviceFunctions.scrapeData(urls[2])
                price = self.serviceFunctions.getPriceWollPlatz(scraped)
                deliveryTime = self.serviceFunctions.getDeliveryTimeWollPlatz(scraped)
                table = self.serviceFunctions.getSpecificationsFromTableWollPlatz(scraped)
                params.update(price)
                params.update(deliveryTime)
                params.update(table)
                self.paramsSaveCsv(buttons[2], params)
                return render_template(render,
                             button1=buttons[0],
                             button2=buttons[1],
                             button3=buttons[2],
                             button4=buttons[3],
                             buttonTag=True,
                             url=urls[2],
                             price=params["price"],
                             deliveryTime=params["deliveryTime"],
                             needleSize=params["needleSize"],
                             composition=params["composition"],
                             )
            elif requestObject.form.get(buttons[3]) == buttons[3]:
                scraped = self.serviceFunctions.scrapeData(urls[3])
                price = self.serviceFunctions.getPriceWollPlatz(scraped)
                deliveryTime = self.serviceFunctions.getDeliveryTimeWollPlatz(scraped)
                table = self.serviceFunctions.getSpecificationsFromTableWollPlatz(scraped)
                params.update(price)
                params.update(deliveryTime)
                params.update(table)
                self.paramsSaveCsv(buttons[3], params)
                return render_template(render,
                             button1=buttons[0],
                             button2=buttons[1],
                             button3=buttons[2],
                             button4=buttons[3],
                             buttonTag=True,
                             url=urls[3],
                             price=params["price"],
                             deliveryTime=params["deliveryTime"],
                             needleSize=params["needleSize"],
                             composition=params["composition"],
                             )
#            elif requestObject.form.get(buttons[4]) == buttons[4]:
#                scraped = self.serviceFunctions.scrapeData(urls[4])
#                price = self.serviceFunctions.getPriceWollPlatz(scraped)
#                deliveryTime = self.serviceFunctions.getDeliveryTimeWollPlatz(scraped)
#                table = self.serviceFunctions.getSpecificationsFromTableWollPlatz(scraped)
#                print(price)
#                print(deliveryTime)
#                print(table)
#                #self.serviceFunctions.printString(buttons[4])
            else:
                return render_template(render,
                             button1=buttons[0],
                             button2=buttons[1],
                             button3=buttons[2],
                             button4=buttons[3],
                             )

        elif requestObject.method == 'GET':
            # return render_template("index.html")
            self.serviceFunctions.printString("No Post Back Call")
