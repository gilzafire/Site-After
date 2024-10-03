#!/bin/sh

python manage.py collectstatic
gunicorn After2125.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 