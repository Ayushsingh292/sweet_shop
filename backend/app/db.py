from motor.motor_asyncio import AsyncIOMotorClient
from config import settings


client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]

users_col = db["users"]
sweets_col = db["sweets"]
