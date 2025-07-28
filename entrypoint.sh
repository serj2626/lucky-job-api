#!/bin/bash
set -e

echo "📦 Применяем миграции..."
alembic upgrade head  # или python manage.py migrate, если Django

echo "🚀 Запускаем Gunicorn..."
exec gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000 --workers 4 --timeout 60
