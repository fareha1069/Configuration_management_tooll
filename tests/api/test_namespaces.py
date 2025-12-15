def test_create_namespace(client):
    response = client.post(
        "/api/namespaces",
        json={"name": "dev"}
    )

    assert response.status_code in (200, 201)


def test_list_namespaces(client):
    response = client.get("/api/namespaces")
    assert response.status_code == 200
    assert isinstance(response.json, list)
