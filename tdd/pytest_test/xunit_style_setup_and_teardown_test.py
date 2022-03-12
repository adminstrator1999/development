"""Every scope example of setup and teardown"""


def setup_module(module):
    print("Setup Module\n")


def teardown_module(module):
    print("Teardown Module\n")


def setup_function(function):
    if function == test1:
        print("\nSetup for function test1")
    elif function == test2:
        print("\nSetup for function test2")
    else:
        print("\nUnknown test")


def teardown_function(function):
    if function == test1:
        print("\nTeardown for function test1")
    elif function == test2:
        print("\nTeardown for function test")
    else:
        print("\nUnknown test")


def test1():
    print("TEST 1 EXECUTED")


def test2():
    print("TEST 2 EXECUTED")


class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass")

    def setup_method(self, method):
        if method == self.test3:
            print("\nSetup for test3")
        elif method == self.test4:
            print("\nSetup for test4")
        else:
            print("\nUnknown method")

    def teardown_method(self, method):
        if method == self.test3:
            print("\nTeardown for test3")
        elif method == self.test4:
            print("\nTeardown for test4")
        else:
            print("\nUnknown method")

    def test3(self):
        print("TEST 3 IS EXECUTED")

    def test4(self):
        print("TEST 4 IS EXECUTED")
