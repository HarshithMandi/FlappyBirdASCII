def test_create_user(client):
    response = client.post("/users/", json={
        "name": "Test User",
        "email": "test@example.com"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200