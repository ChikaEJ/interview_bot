from aiogram.types import Message

from app.ai.open_ia import ask_question


async def on_start(message: Message):
    await message.answer("Hello!!!")

async def on_ask_question(message: Message):
    question = message.text
    user_id = message.from_user.id
    response = await ask_question(user_id=user_id, question=question)
    await message.answer(response)
