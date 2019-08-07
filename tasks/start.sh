#!/usr/bin/env bash
cd ../mummy-money
npm start &
cd ../backend
python3 manage.py runserver
