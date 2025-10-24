from aiogram.types import Message


async def on_start(message: Message):
    await message.answer("Hello!!!")