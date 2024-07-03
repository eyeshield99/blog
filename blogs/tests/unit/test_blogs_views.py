import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_views_GET(client) -> None:
    test_cases = [
        ("blog-index", 200),
    ]
    for tc in test_cases:
        name, status_code = tc
        url = reverse(name)
        response = client.get(url)
        assert response.status_code == status_code
