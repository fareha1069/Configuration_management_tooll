def test_create_resource(client):
    client.post("/api/namespaces", json={"name": "prod"})

    response = client.post(
        "/api/resources",
        json={
            "name": "api-key",
            "arn": "arn:prod",
            "value": "123",
            "resource_type": "secret",
            "namespace": "prod"
        }
    )

    assert response.status_code in (200, 201)


def test_list_resources(client):
    response = client.get("/api/resources")
    assert response.status_code == 200
