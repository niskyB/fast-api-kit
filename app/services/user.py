import logging

from app.api.api_v1.endpoints.deps import graph_client
from app.models.user import UserProperties
from app.schemas.user import UserQueryParams


logger = logging.getLogger(__name__)

users_url = "/users"


class UserService:
    async def list_users(self, params: UserQueryParams):
        select_properties = ""
        user_properties_list = list(UserProperties)

        for i, e in enumerate(user_properties_list):
            select_properties += f"{e.value}"
            if i < len(user_properties_list) - 1:
                select_properties += ","

        url = f"/{users_url}?$select={select_properties}"
        if params.value:
            url += f"&$filter=startsWith(mail, '{params.value}') OR startsWith(displayName, '{params.value}')"

        users = graph_client.get(
            url,
        )
        return users.json().get("value")
