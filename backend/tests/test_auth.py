import pytest

@pytest.mark.asyncio
async def test_register_and_login(client):
    r = await client.post("/api/auth/register", json={
        "email": "user@test.com", "password": "User123!", "name": "User"
    })
    assert r.status_code == 201

    r2 = await client.post("/api/auth/login", json={
        "email": "user@test.com", "password": "User123!"
    })
    assert r2.status_code == 200
    data = r2.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    me = await client.get("/api/auth/me", headers={"Authorization": f"Bearer {data['access_token']}"})
    assert me.status_code == 200
    assert me.json()["email"] == "user@test.com"
