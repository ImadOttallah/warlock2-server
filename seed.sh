#!/bin/bash
rm -rf levelupapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations warlockapi
python3 manage.py migrate warlockapi
python3 manage.py loaddata users
python3 manage.py loaddata npc_types
python3 manage.py loaddata cast_types
python3 manage.py loaddata npc_categories
python3 manage.py loaddata cast_categories
python3 manage.py loaddata npcs
python3 manage.py loaddata cast
python3 manage.py loaddata characters
python3 manage.py loaddata campaigns
python3 manage.py loaddata npc_campaigns
python3 manage.py loaddata cast_campaigns
