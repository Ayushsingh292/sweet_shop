import pytest_asyncio
import asyncio
import os
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from app.main import app


@pytest_asyncio.fixture(scope="session")
def event_loop():
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="session", autouse=True)
def set_test_env():
    os.environ["MONGO_DB"] = "sweetshop_test"

@pytest_asyncio.fixture
async def client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac
