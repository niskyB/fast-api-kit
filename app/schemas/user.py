from typing_extensions import Annotated
from pydantic import BaseModel
from fastapi import Query


class UserQueryParams(BaseModel):
    value: Annotated[str, Query()] = ""
