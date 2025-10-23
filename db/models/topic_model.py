
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class Topic(Base):

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="topics")

    questions: Mapped[list["Question"]] = relationship("Question", back_populates="topic", cascade="all, delete")

    def __repr__(self):
        return f"<Topic {self.title}>"
