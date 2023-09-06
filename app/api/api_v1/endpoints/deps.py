from msgraph.core import APIVersion, GraphClient
from azure.identity import ClientSecretCredential
from app.core import settings

graph_client = GraphClient(
    credential=ClientSecretCredential(
        tenant_id=settings.TENANT_ID,
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
    ),
    api_version=APIVersion.beta,
)
