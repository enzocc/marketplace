#!/bin/bash -e

echo "Waiting for database"
python3 wait_for_db.py

echo "Running migrations"
alembic upgrade head

gunicorn -k gthread --bind 0.0.0.0:5000 --workers 2 --threads 2 --reload --access-logfile - app.main:app
