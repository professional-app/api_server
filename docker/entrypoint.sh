#!/bin/sh

set -x
API_PATH="/var/www/html/api_project"

"$API_PATH"/manage.py makemigrations
"$API_PATH"/manage.py migrate

exec "$@"
