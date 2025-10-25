import json
from redis.asyncio import Redis
from app.core.config import settings

REDIS_HOST = settings.REDIS_HOST
REDIS_PORT = settings.REDIS_PORT

redis = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=0,
    decode_responses=True
)

async def get_history(user_id: int) -> list:
    data = await redis.get(f"chat_history:{user_id}")
    if data:
        return json.loads(data)
    return [{"role": "system", "content": "Ты специалист по языку программирования Python."}]

async def save_history(user_id: int, history: list):
    trimmed = history[-10:]
    await redis.set(f"chat_history:{user_id}", json.dumps(trimmed))
