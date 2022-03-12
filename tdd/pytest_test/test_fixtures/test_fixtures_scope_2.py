import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_module2():
    print("\nSetup Module2")


@pytest.fixture(scope="class", autouse=True)
def setup_class2():
    """class level scope"""
    print("\nSetup Class2")


@pytest.fixture(scope="function", autouse=True)
def setup_function2():
    """function level scope"""
    print("\nSetup Function2")


class TestClass:
    def test_it(self):
        print("Test it 1")
        assert True

    def test_it_2(self):
        print("Test it 2")
        assert True
