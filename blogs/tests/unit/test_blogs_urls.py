import pytest
from django.conf import settings
from django.urls import resolve, reverse


def test_all_static_pages() -> None:
    test_cases = [
        ("blog-index", "/"),
    ]
    for tc in test_cases:
        name, url = tc
        assert reverse(name) == url
        assert resolve(url).view_name == name
