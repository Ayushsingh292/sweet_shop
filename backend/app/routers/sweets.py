from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from ..db import sweets_col
from ..schemas import SweetCreate, SweetUpdate, RestockIn
from ..models import to_str_id
from ..dependencies import get_current_user, require_admin

router = APIRouter(prefix="/api/sweets", tags=["sweets"])

@router.post("", status_code=201)
async def create_sweet(body: SweetCreate, _=Depends(require_admin)):
    doc = body.model_dump()
    res = await sweets_col.insert_one(doc)
    created = await sweets_col.find_one({"_id": res.inserted_id})
    return to_str_id(created)

@router.get("")
async def list_sweets(_=Depends(get_current_user)):
    cursor = sweets_col.find({})
    return [to_str_id(doc) async for doc in cursor]

@router.get("/search")
async def search_sweets(name: str | None = None, category: str | None = None,
                        min_price: float | None = None, max_price: float | None = None,
                        _=Depends(get_current_user)):
    q = {}
    if name: q["name"] = {"$regex": name, "$options": "i"}
    if category: q["category"] = {"$regex": category, "$options": "i"}
    price = {}
    if min_price is not None: price["$gte"] = min_price
    if max_price is not None: price["$lte"] = max_price
    if price: q["price"] = price
    cursor = sweets_col.find(q)
    return [to_str_id(doc) async for doc in cursor]

@router.put("/{sid}")
async def update_sweet(sid: str, body: SweetUpdate, _=Depends(require_admin)):
    if not ObjectId.is_valid(sid):
        raise HTTPException(status_code=400, detail="Invalid id")
    update = {k: v for k, v in body.model_dump(exclude_none=True).items()}
    await sweets_col.update_one({"_id": ObjectId(sid)}, {"$set": update})
    doc = await sweets_col.find_one({"_id": ObjectId(sid)})
    if not doc:
        raise HTTPException(status_code=404, detail="Sweet not found")
    return to_str_id(doc)

@router.delete("/{sid}", status_code=204)
async def delete_sweet(sid: str, _=Depends(require_admin)):
    if not ObjectId.is_valid(sid):
        raise HTTPException(status_code=400, detail="Invalid id")
    await sweets_col.delete_one({"_id": ObjectId(sid)})
    return

@router.post("/{sid}/purchase")
async def purchase_sweet(sid: str, _=Depends(get_current_user)):
    if not ObjectId.is_valid(sid):
        raise HTTPException(status_code=400, detail="Invalid id")
    doc = await sweets_col.find_one({"_id": ObjectId(sid)})
    if not doc:
        raise HTTPException(status_code=404, detail="Not found")
    if doc["quantity"] <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")
    await sweets_col.update_one({"_id": doc["_id"]}, {"$inc": {"quantity": -1}})
    updated = await sweets_col.find_one({"_id": doc["_id"]})
    return to_str_id(updated)

@router.post("/{sid}/restock")
async def restock_sweet(sid: str, body: RestockIn, _=Depends(require_admin)):
    if not ObjectId.is_valid(sid):
        raise HTTPException(status_code=400, detail="Invalid id")
    await sweets_col.update_one({"_id": ObjectId(sid)}, {"$inc": {"quantity": body.amount}})
    updated = await sweets_col.find_one({"_id": ObjectId(sid)})
    if not updated:
        raise HTTPException(status_code=404, detail="Not found")
    return to_str_id(updated)
