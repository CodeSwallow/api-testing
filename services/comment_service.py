from services import base_service


class CommentService(base_service.BaseService):

    def __init__(self):
        self.BASE_URL += '/comments'
