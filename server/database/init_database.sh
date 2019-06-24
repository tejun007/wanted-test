#!/usr/bin/env bash
cd /server
python database/manage.py db upgrade

cd database
python init_mariadb_dataset.py

