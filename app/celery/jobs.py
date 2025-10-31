import asyncio

from app.celery.celery_app import celery_app

@celery_app.task(max_retries=3, default_retry_delay=10)
async def send_question():
    asyncio.run(_send_question())


async def _send_question():
    return "Hello, I am here!"