#!/bin/bash
# run this inside the vagrant machine once started

# create venv virtual environment in folder ~/venv
python3 -m venv ~/venv

# activate the virtual environment
source ~/venv/bin/activate

# install django
pip install django
pip install --upgrade pip
# cd test_01/test_project_01/
# python manage.py runserver 0:8080