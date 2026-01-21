def test_create_todo(client):
    response = client.post(
        "/api/v1/todos/",
        json={"title": "Integration Todo"},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Integration Todo"
    assert data["completed"] is False


def test_list_todos(client):
    response = client.get("/api/v1/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
