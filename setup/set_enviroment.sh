#!/bin/bash

which python3

if [ $? -eq 1 ]
then echo "Python3 is not installed" && exit
fi

sudo apt-get install unzip

pip3 install flask
pip3 install requests
pip3 install bs4
pip3 install mock
pip3 install xmlrunner
pip3 install selenium
pip3 install webdriver-manager
pip3 install numpy

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
unzip chromedriver_linux64.zip