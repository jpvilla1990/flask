# flask

# Introduction

This project allows to obtain the price, delivery time, needle size and composition of the following products:
            "DMC-NaturaXL"
            "Drops-Safran"
            "Drops-BabyMerinoMix"
            "Stylecraft-SpecialDoubleKnit"
as a note the product "Hahn-AlpaccaSpeciale" could not be found in the specified website, therefore it was not included.

# Setup

In order to setup this webapplication, python 3.6 must be present, and then in the folder "setup" the following script must be
executed:
`set_enviroment.sh`
This bash script will install all the needed packages

# Usage

Currently a website is generated in localhost:8050, to do so, after being located in the main folder "flask", execute the following command:
`python3 appMain.py`
this command will start the website.
After clicking on each product, the website will display the aforementioned information on the same website, additionally a csv file will
be generated for every product in the folder "results"

# Tests

There are two type of tests, unittests and functionaltests in the folder "test", the first ones can be executed as follow:
`python3 app_unittests.py`
This unittests will mock some function to guarantee isolation when testing the inner functions that makes the website functional,
the functions under test are basically those that scrape the website target where the info is obtained, but since the methods are
mocked, the unittest works even if there is not internet and the application is not runnijg

The functional tests before being execute, the application must be started beforehand, it is crucial to execute the set_enviroment.sh 
script. This functional tests are designed to work only in linux enviroment
`python3 app_functionaltest.py`
These functional tests will use selenium to automatically click over each button of interest (every product), and it will verify if
the corresponding csv file is generated or not.

# Architecture

The project was develop using a appMain.py file to contain the url routes, an routeFunctions.py file located in tools to contain the
code for the function corresponding to the routes. And a serviceFunctions.py located in tools which have functional methods that are
called in route functions.
In order to make the project incrementalable this architecture was created. Therefore if new routes are created it is easy to locate them
and if more functions are needed for the internal functionallity, the previous modularity enables more simplication and easy comprehension.

