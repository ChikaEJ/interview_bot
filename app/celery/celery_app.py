from celery import Celery

celery_app = Celery(
    main="interview_bot_agent",
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=["app.celery.jobs"]
)

celery_app.conf.beat_schedule = {
    "ask question": {
        "task": "interview_bot_agent.ask_question",
        "schedule": 60
    }
}