from datetime import datetime
from pydantic import BaseModel, Field

from app.db.schemas.base_schemas import BaseSchema


class TopicCreate(BaseModel):
    title: str = Field(..., max_length=100)
    description: str | None = None
    user_id: int

class TopicRead(BaseSchema):
    id: int
    title: str
    description: str | None
    created_at: datetime
