from app.db.controllers.base_crud import BaseCRUD
from app.db.models.user_model import User
from app.db.schemas.user_schemas import UserCreate, UserRead


class UserController(BaseCRUD[User, UserCreate, UserRead]):
    def __init__(self):
        super().__init__(User, UserRead)

user_controller = UserController()