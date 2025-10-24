from aiogram import Dispatcher
from aiogram.filters import CommandStart

from app.bot.selected.selected import on_start


def register_handlers(dp: Dispatcher):
    dp.message.register(on_start, CommandStart())