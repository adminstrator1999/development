import pytest


def raises_value_exception():
    raise ValueError


def test_exception():
    with pytest.raises(ValueError):
        raises_value_exception()
