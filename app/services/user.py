import logging

from app.repositories.user import UserRepository

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_user_by_id(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id=user_id)
