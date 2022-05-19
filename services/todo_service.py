from services import base_service


class TodoService(base_service.BaseService):

    def __init__(self):
        self.BASE_URL += '/todos'
