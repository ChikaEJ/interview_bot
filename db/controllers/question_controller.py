from db.controllers.base_crud import BaseCRUD
from db.models.question_model import Question
from db.schemas.question_schemas import QuestionCreate, QuestionRead


class QuestionController(BaseCRUD[Question, QuestionCreate, QuestionRead]):
    def __init__(self):
        super().__init__(Question, QuestionRead)

question_controller = QuestionController()