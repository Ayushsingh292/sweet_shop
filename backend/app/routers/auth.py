from fastapi import APIRouter, HTTPException, status, Depends
from ..schemas import UserCreate, LoginIn, TokenOut
from ..db import users_col
from ..security import hash_password, verify_password, create_access_token
from ..dependencies import get_current_user

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register", status_code=201)
async def register(body: UserCreate):
    exists = await users_col.find_one({"email": body.email})
    if exists:
        raise HTTPException(status_code=409, detail="Email already registered")
    doc = {
        "email": body.email,
        "name": body.name,
        "password": hash_password(body.password),
        "role": body.role or "user",
    }
    await users_col.insert_one(doc)
    return {"message": "registered"}

@router.post("/login", response_model=TokenOut)
async def login(body: LoginIn):
    user = await users_col.find_one({"email": body.email})
    if not user or not verify_password(body.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(user["email"], user.get("role", "user"))
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
async def me(user = Depends(get_current_user)):
    return user
