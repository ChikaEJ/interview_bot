from aiogram import Dispatcher, F
from aiogram.filters import CommandStart

from app.bot.selected.selected import on_ask_question, on_start


def register_handlers(dp: Dispatcher):
    dp.message.register(on_start, CommandStart())
    dp.message.register(on_ask_question, F.text)
