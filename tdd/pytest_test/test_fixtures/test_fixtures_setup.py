"""Most examples of fixtures"""
import pytest


"""There are two ways of calling fixtures"""


@pytest.fixture()
def setup():
    """declaring setup fixture"""
    print("\nSetup")


def test1(setup):
    """The first way is passing setup fixture as an argument to test u want"""
    print("Executing test1")
    assert True


@pytest.mark.usefixtures("setup")
def test2():
    """The second way is using 'pytest.mark.usefixtures'
    and passing it the setup function as a string argument"""
    print("Executing test2")
    assert True
