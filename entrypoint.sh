#!/bin/sh
python manage.py migrate
uwsgi --http 0.0.0.0:8000 --wsgi-file webcollector/wsgi.py
exec "$@"