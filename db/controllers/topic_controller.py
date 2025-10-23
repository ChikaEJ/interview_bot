from db.controllers.base_crud import BaseCRUD
from db.models.topic_model import Topic
from db.schemas.topoc_schemas import TopicCreate, TopicRead


class TopicController(BaseCRUD[Topic, TopicCreate, TopicRead]):
    def __init__(self):
        super().__init__(Topic, TopicRead)

topic_controller = TopicController()