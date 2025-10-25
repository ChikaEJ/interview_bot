import asyncio
from logging.config import fileConfig
from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings
from app.core.db import Base
from app.db.models import *

models = [User, Progress, Topic, Question]

# Alembic Config object
config = context.config

# Настраиваем URL из настроек
db_url = settings.DATABASE_URL
if db_url and db_url != "DATABASE_URL":
    config.set_main_option("sqlalchemy.url", db_url)

# Настройка логов Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Метаданные для автогенерации миграций
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Синхронное выполнение миграций через run_sync"""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' (async) mode."""
    connectable = create_async_engine(settings.DATABASE_URL, poolclass=pool.NullPool)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
