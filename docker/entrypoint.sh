#!/bin/sh

set -x
set -e

API_PATH="/var/www/html/api_project"
ENV_FILE="/opt/api.env"

cd $API_PATH

source $ENV_FILE

until psql $DATABASE_URL -c '\l'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - continuing"

#Do this every time, even though its wasteful on startup.
python manage.py makemigrations
python manage.py migrate --noinput

exec "python manage.py $@"
