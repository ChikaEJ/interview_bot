from app.db.controllers.base_crud import BaseCRUD
from app.db.models.topic_model import Topic
from app.db.schemas.topoc_schemas import TopicCreate, TopicRead


class TopicController(BaseCRUD[Topic, TopicCreate, TopicRead]):
    def __init__(self):
        super().__init__(Topic, TopicRead)

topic_controller = TopicController()