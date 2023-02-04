#!/bin/bash
rm -rf levelupapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations warlockapi
python3 manage.py migrate warlockapi
python3 manage.py loaddata users
python3 manage.py loaddata npctypes
python3 manage.py loaddata casttypes
python3 manage.py loaddata npccategories
python3 manage.py loaddata castcategories
python3 manage.py loaddata npcs
python3 manage.py loaddata cast
python3 manage.py loaddata characters
python3 manage.py loaddata campaigns
python3 manage.py loaddata npccampaigns
python3 manage.py loaddata castcampaigns
