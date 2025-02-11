#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3 python3.12-venv python3-pip
sudo apt install -y git
ssh -o StrictHostKeyChecking=no git@github.com
git clone https://github.com/Gatche-clyb/el.git $HOME/el
cd el
python3 -m venv el
. el/bin/activate
pip install colorama
pip install pandas
pip install matplotlib
pip install seaborn
