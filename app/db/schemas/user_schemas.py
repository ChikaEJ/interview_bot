from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

from app.db.schemas.base_schemas import BaseSchema


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserRead(BaseSchema):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
