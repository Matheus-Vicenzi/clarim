#!/bin/sh
# aplica migrations
python manage.py migrate --noinput
# inicia o gunicorn (ou outro servidor)
exec gunicorn clarim.wsgi:application --bind 0.0.0.0:8000
