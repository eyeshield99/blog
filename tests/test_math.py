from app.math import multiply_two_numbers


def test_multiply_two_numbers() -> None:
    have = multiply_two_numbers(2, 3)
    want = 6
    assert have == want
