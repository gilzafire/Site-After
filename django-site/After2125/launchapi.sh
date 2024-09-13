#!/bin/sh

python manage.py migrate
# Start Gunicorn server with Django app
exec gunicorn api.wsgi:application \
    --bind 0.0.0.0:8001 \
    --workers 3  # You can adjust the number of workers based on your server