#!/bin/bash

which python3

if [ $? -eq 1 ]
then echo "Python3 is not installed" && exit
fi

pip3 install flask
pip3 install requests
pip3 install bs4
pip3 install mock
pip3 install xmlrunner