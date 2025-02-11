#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3 python3.12-venv python3-pip
sudo apt install -y git
git clone git@github.com:Gatche-clyb/el.git $HOME/el
cd el
python -m venv el
. el/bin/activate
pip install colorama
pip instal pandas
pip install matplotlib
pip install seaborn
