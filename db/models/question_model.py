
from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class Question(Base):

    text: Mapped[str] = mapped_column(Text, nullable=False)
    answer: Mapped[str] = mapped_column(Text, nullable=True)
    difficulty: Mapped[int] = mapped_column(Integer, nullable=True)  # 1-5

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="questions")
    topic: Mapped["Topic"] = relationship("Topic", back_populates="questions")
    progress: Mapped[list["Progress"]] = relationship("Progress", back_populates="question", cascade="all, delete")

    def __repr__(self):
        return f"<Question {self.id}>"
