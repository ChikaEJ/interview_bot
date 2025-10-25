from openai import AsyncOpenAI, RateLimitError
from app.core.config import settings
from app.redis.redis import get_history, save_history

client = AsyncOpenAI(
    base_url=settings.AI_BASE_URL,
    api_key=settings.OPENAI_API_KEY
)

async def ask_question(user_id: int, question: str) -> str:
    try:
        history = await get_history(user_id)

        history.append({"role": "user", "content": question})

        response = await client.chat.completions.create(
            model=settings.AI_MODEL,
            messages=history
        )

        answer = response.choices[0].message.content

        history.append({"role": "assistant", "content": answer})

        await save_history(user_id, history)

        return answer

    except RateLimitError:
        return "⚠️ Лимит запросов к AI исчерпан. Попробуйте позже."
    except Exception as e:
        return f"❌ Ошибка: {e}"
