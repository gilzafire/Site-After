#!/bin/sh

pytons mange.py migrate
# Start Gunicorn server with Django app
exec gunicorn public.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3  # You can adjust the number of workers based on your server