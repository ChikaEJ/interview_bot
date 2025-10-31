#!/usr/bin/env sh
set -e

echo "⏳ Ожидание базы данных ${POSTGRES_HOST}:${POSTGRES_PORT}..."
until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  echo "⏳ База данных недоступна, пробуем снова..."
  sleep 2
done

echo "✅ База данных доступна!"

echo "🚀 Запуск миграций Alembic..."
alembic upgrade head

echo "🎯 Запуск приложения: $@"
exec "$@"