from dependency_injector import containers, providers

from app.core import settings
from app.db.database import Database


# Please import Container class directly from this file if you want to use it in another file.
# Don't import it from __init__.py in the "core" folder.
# This is for the pytest to run.
class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[])

    db = providers.Singleton(Database, db_url=settings.SQLALCHEMY_DATABASE_URL)
