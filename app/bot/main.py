from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from app.bot.handlers import register_handlers
from app.core.config import settings

bot = Bot(settings.BOT_TOKEN)
REDIS_HOST = settings.REDIS_HOST
REDIS_PORT = settings.REDIS_PORT
redis = Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)


async def bot_main():
    dp = Dispatcher(storage=RedisStorage(redis), bot=bot)
    register_handlers(dp)

    await dp.start_polling(bot)
