#!/bin/sh

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$CLEANSTART" = 1 ]
then
    echo "Flush and migrate db"
    python manage.py flush --no-input
    python manage.py migrate
fi

exec "$@"