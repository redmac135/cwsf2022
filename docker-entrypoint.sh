#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

export DJANGO_SETTINGS_MODULE=cwsf.settings.production

python manage.py migrate
python manage.py loaddata */fixtures/*.json
python manage.py runserver 0.0.0.0:$PORT

exec "$@"