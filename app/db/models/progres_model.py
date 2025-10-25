
from sqlalchemy import Float, ForeignKey, Integer, Text, \
    UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Progress(Base):

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    question_id: Mapped[int] = mapped_column(
        ForeignKey("question.id", ondelete="CASCADE"), nullable=False)

    score: Mapped[float] = mapped_column(Float, nullable=False)  # 0.0–1.0
    is_correct: Mapped[bool] = mapped_column(default=False)
    attempt: Mapped[int] = mapped_column(Integer, default=1)
    comment: Mapped[str] = mapped_column(Text, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="progress")
    question: Mapped["Question"] = relationship("Question",
                                                back_populates="progress")

    __table_args__ = (
        UniqueConstraint("user_id", "question_id", "attempt",
                         name="uq_user_question_attempt"),
    )

    def __repr__(self):
        return f"<Progress user={self.user_id}, question={self.question_id}, score={self.score}>"
