import uvicorn
from fastapi import status

from app.core import http_client
from app.factory import create_app

app = create_app()


@app.on_event("startup")
async def load_config() -> None:
    """
    Load OpenID config on startup.
    """


@app.on_event("shutdown")
async def shutdown_event():
    await http_client.close()


@app.get("/", tags=["Heath Check"], status_code=status.HTTP_200_OK)
async def health_check():
    return "Service runs well"


@app.get("/api/v1/version", tags=["Heath Check"], status_code=status.HTTP_200_OK)
async def get_version():
    return "v0.1 2023/08/24"


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
