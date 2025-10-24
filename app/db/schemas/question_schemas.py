from datetime import datetime
from pydantic import BaseModel, Field

from app.db.schemas.base_schemas import BaseSchema


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=3)
    answer: str | None = None
    difficulty: int | None = Field(None, ge=1, le=5)
    user_id: int
    topic_id: int

class QuestionRead(BaseSchema):
    id: int
    text: str
    answer: str | None
    difficulty: int | None
    created_at: datetime
