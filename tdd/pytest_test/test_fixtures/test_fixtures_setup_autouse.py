"""Most examples of fixtures"""
import pytest


@pytest.fixture(autouse=True)
def setup():
    """We can use autouse to pass fixtures to every functions"""
    print("\nSetup Auto_use")


def test1():
    print("Executing test1")
    assert True


def test2():
    print("Executing test2")
    assert True
