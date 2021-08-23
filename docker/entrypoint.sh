#!/bin/sh

set -x
set -e

API_PATH="/var/www/html/api_project"
cd $API_PATH

#Do this every time, even though its wasteful on startup.
python manage.py makemigrations
python manage.py migrate --noinput

exec "python manage.py $@"
