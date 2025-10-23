from db.controllers.base_crud import BaseCRUD
from db.models.progres_model import Progress
from db.schemas.progress_schemas import ProgressCreate, ProgressRead


class ProgressController(BaseCRUD[Progress, ProgressCreate, ProgressRead]):
    def __init__(self):
        super().__init__(Progress, ProgressRead)

progress_controller = ProgressController()