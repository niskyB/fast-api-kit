import logging

from fastapi import HTTPException, status
from app.constants.error_message import SOMETHING_WENT_WRONG

from app.models import User
from app.repositories.base import BaseRepository

logger = logging.getLogger(__name__)


class UserRepository(BaseRepository[User]):
    def __init__(self, get_session):
        super().__init__(entity=User, get_session=get_session)

    def get_user_by_id(self, user_id: int):
        with self.get_session() as session:
            try:
                user: User = session.query(User).filter(User.id == user_id).first()
                return user
            except Exception as e:
                logger.error(e)
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=SOMETHING_WENT_WRONG,
                )
