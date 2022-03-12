import pytest


@pytest.fixture()
def setup1():
    """we can use yield keyword to specify teardown method"""
    print("\nSetup1")
    yield
    print("\nTeardown")


@pytest.fixture()
def setup2(request):
    """we can use request context and addfinalizer method
    to specify multiple teardown functions"""
    print("\nSetup2")

    def teardown_a():
        print("Teardown_a")

    def teardown_b():
        print("\nTeardown_b")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    print("Test1 is executed")


def test2(setup2):
    print("Test2 is executed")
