from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, sweets
from .db import users_col
from .security import hash_password

app = FastAPI(title="Sweet Shop API", version="1.0.0")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    # Ensure default admin exists (email/pass below)
    if not await users_col.find_one({"email": "admin@sweet.com"}):
        await users_col.insert_one({
            "email": "admin@sweet.com",
            "name": "Admin",
            "password": hash_password("Admin123!"),
            "role": "admin",
        })

app.include_router(auth.router)
app.include_router(sweets.router)
