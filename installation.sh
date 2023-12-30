#!/bin/bash

#check currently install python version
python3 --version
#Use advance packaging tool (apt) to update
sudo apt update
#even after update latest version will not be available to install
sudo apt-get install sofware-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
#install python latest version
sudo apt-get install python3.12


