from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.core.security import hash_password, verify_password


class User(Base):

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    topics: Mapped[list["Topic"]] = relationship("Topic", back_populates="user", cascade="all, delete")
    questions: Mapped[list["Question"]] = relationship("Question", back_populates="user", cascade="all, delete")
    progress: Mapped[list["Progress"]] = relationship("Progress", back_populates="user", cascade="all, delete")

    def set_password(self, password: str):
        self.password_hash = hash_password(password)

    def check_password(self, password: str) -> bool:
        return verify_password(password, self.password_hash)

    def __repr__(self):
        return f"<User {self.username}>"
