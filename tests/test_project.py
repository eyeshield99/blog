from app import __version__


def test_version() -> None:
    have = __version__
    want = "0.1.0"
    assert have == want
