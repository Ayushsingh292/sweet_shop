import pytest

@pytest.mark.asyncio
async def test_sweets_crud_and_inventory(client):
    # login preseeded admin
    admin_login = await client.post("/api/auth/login", json={
        "email": "admin@sweet.com", "password": "Admin123!"
    })
    assert admin_login.status_code == 200
    admin_token = admin_login.json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}

    # create sweet (admin)
    create = await client.post("/api/sweets", json={
        "name": "Ladoo", "category": "Indian", "price": 15.0, "quantity": 10
    }, headers=admin_headers)
    assert create.status_code == 201
    sweet = create.json()

    # list
    lst = await client.get("/api/sweets", headers=admin_headers)
    assert lst.status_code == 200
    assert any(s["name"] == "Ladoo" for s in lst.json())

    # search
    srch = await client.get("/api/sweets/search?category=Indian", headers=admin_headers)
    assert srch.status_code == 200
    assert len(srch.json()) >= 1

    # update price
    up = await client.put(f"/api/sweets/{sweet['_id']}", json={"price": 20.0}, headers=admin_headers)
    assert up.status_code == 200
    assert up.json()["price"] == 20.0

    # register normal user & purchase
    await client.post("/api/auth/register", json={
        "email": "user2@test.com", "password": "User123!", "name": "User2"
    })
    user_login = await client.post("/api/auth/login", json={
        "email": "user2@test.com", "password": "User123!"
    })
    user_token = user_login.json()["access_token"]
    user_headers = {"Authorization": f"Bearer {user_token}"}

    pur = await client.post(f"/api/sweets/{sweet['_id']}/purchase", headers=user_headers)
    assert pur.status_code == 200
    assert pur.json()["quantity"] == 9

    # restock (admin)
    res = await client.post(f"/api/sweets/{sweet['_id']}/restock", json={"amount": 5}, headers=admin_headers)
    assert res.status_code == 200
    assert res.json()["quantity"] == 14

    # delete (admin)
    d = await client.delete(f"/api/sweets/{sweet['_id']}", headers=admin_headers)
    assert d.status_code == 204
