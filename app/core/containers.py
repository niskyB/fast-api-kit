from dependency_injector import containers, providers

from app.core import settings
from app.db.database import Database
from app.repositories.user import UserRepository
from app.services.user import UserService


# Please import Container class directly from this file if you want to use it in another file.
# Don't import it from __init__.py in the "core" folder.
# This is for the pytest to run.
class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.api_v1.endpoints.user",
        ]
    )

    db = providers.Singleton(Database, db_url=settings.SQLALCHEMY_DATABASE_URL)

    user_repository = providers.Factory(
        UserRepository, get_session=db.provided.get_session
    )

    user_service = providers.Factory(UserService, user_repository=user_repository)
