from sqlalchemy import String, Boolean
from app.models.base_model import BaseModel
from sqlalchemy.orm import mapped_column
from app.db import Base


class User(Base, BaseModel):
    __tablename__ = "user"
    name = mapped_column(String(50), nullable=False)
    isActive = mapped_column(Boolean, default=False, nullable=False)
