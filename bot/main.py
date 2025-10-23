import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from bot.handlers import register_handlers
from core.config import settings

bot = Bot(settings.BOT_TOKEN)
redis = Redis(host='localhost', port=6379, db=0)


async def main():
    dp = Dispatcher(storage=RedisStorage(redis), bot=bot)
    register_handlers(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
