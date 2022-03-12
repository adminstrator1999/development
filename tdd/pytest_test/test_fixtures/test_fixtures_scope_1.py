import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_session():
    """session level scope, the biggest one"""
    print("\nSetup Session")


@pytest.fixture(scope="module", autouse=True)
def setup_module():
    """module level scope"""
    print("\nSetup Module")


@pytest.fixture(scope="function", autouse=True)
def setup_function():
    print("\nSetup FUNCTION")


def test1():
    print("Executing test1!")
    assert True


def test2():
    print("Executing test2")
    assert True
