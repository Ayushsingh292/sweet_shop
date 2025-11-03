from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.config import settings
from app.db import users_col

bearer = HTTPBearer(auto_error=True)

async def get_current_user(token: HTTPAuthorizationCredentials = Depends(bearer)):
    try:
        payload = jwt.decode(token.credentials, settings.JWT_SECRET, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token payload")
    
    user = await users_col.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return {"email": user["email"], "name": user["name"], "role": user.get("role", "user")}

def require_admin(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return user
