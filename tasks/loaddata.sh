#!/usr/bin/env bash

cd ../backend
python3 manage.py loaddata mummy_money/investors/fixtures/fixture
cd -
