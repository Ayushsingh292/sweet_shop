import os
from pydantic import BaseModel

class Settings(BaseModel):
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB: str = os.getenv("MONGO_DB", "sweetshop")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change-me")
    JWT_EXPIRES_MIN: int = int(os.getenv("JWT_EXPIRES_MIN", "60"))

settings = Settings()
