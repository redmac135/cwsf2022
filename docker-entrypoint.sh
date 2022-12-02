#!/bin/sh

export DJANGO_SETTINGS_MODULE=cwsf.settings.production

python manage.py migrate
python manage.py runserver 0.0.0.0:$PORT

exec "$@"