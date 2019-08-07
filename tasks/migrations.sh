#!/usr/bin/env bash
cd ../backend
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
cd -
