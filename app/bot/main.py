from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from app.bot.handlers import register_handlers
from app.core.config import settings
from app.redis.redis import redis

bot = Bot(settings.BOT_TOKEN)


async def bot_main():
    dp = Dispatcher(storage=RedisStorage(redis), bot=bot)
    register_handlers(dp)

    await dp.start_polling(bot)
