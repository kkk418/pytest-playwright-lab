import pytest
from pydantic import BaseModel, ConfigDict


class Post(BaseModel):
    model_config = ConfigDict(extra="ignore")

    userId: int
    id: int
    title: str
    body: str


@pytest.mark.api
@pytest.mark.external
@pytest.mark.smoke
def test_get_post_returns_expected_contract(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200
    post = Post.model_validate(response.json())
    assert post.id == 1
    assert post.userId > 0
    assert post.title


@pytest.mark.api
@pytest.mark.external
@pytest.mark.regression
@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_filter_posts_by_user(api_client, user_id: int):
    response = api_client.get("/posts", params={"userId": user_id})

    assert response.status_code == 200
    posts = [Post.model_validate(item) for item in response.json()]
    assert posts
    assert all(post.userId == user_id for post in posts)


@pytest.mark.api
@pytest.mark.external
@pytest.mark.regression
def test_unknown_post_returns_not_found(api_client):
    response = api_client.get("/posts/9999")

    assert response.status_code == 404


@pytest.mark.api
@pytest.mark.external
@pytest.mark.regression
def test_create_post_returns_created_resource(api_client):
    payload = {"title": "pytest practice", "body": "contract test", "userId": 1}

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201
    created = Post.model_validate(response.json())
    assert created.title == payload["title"]
    assert created.userId == payload["userId"]

