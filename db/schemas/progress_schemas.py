from datetime import datetime
from pydantic import BaseModel, Field

from db.schemas.base_schemas import BaseSchema


class ProgressCreate(BaseModel):
    user_id: int
    question_id: int
    score: float = Field(..., ge=0.0, le=1.0)
    is_correct: bool = False
    attempt: int = 1
    comment: str | None = None

class ProgressRead(BaseSchema):
    id: int
    user_id: int
    question_id: int
    score: float
    is_correct: bool
    attempt: int
    comment: str | None
    created_at: datetime
