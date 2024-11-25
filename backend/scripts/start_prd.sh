#!/bin/bash

echo "    _______________ _________    __    __________  ____  ______"
echo "   / ____/  _/ ___// ____/   |  / /   / ____/ __ \/ __ \/ ____/"
echo "  / /_   / / \__ \/ /   / /| | / /   / /   / / / / / / / __/   "
echo " / __/ _/ / ___/ / /___/ ___ |/ /___/ /___/ /_/ / /_/ / /___   "
echo "/_/   /___//____/\____/_/  |_/_____/\____/\____/_____/_____/   "

source .env  # Source the .env file (Linux/macOS)

# Run Django migrations
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py makemigrations api
python manage.py makemigrations weather
python manage.py migrate --no-input

# Create superuser
python manage.py createsuperuser --noinput
# Run initial data
python scripts/initial_data.py

# Run Django server via Gunicorn
gunicorn fiscal_code.wsgi -b 0.0.0.0:8000