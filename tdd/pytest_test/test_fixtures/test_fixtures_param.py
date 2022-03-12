import pytest


@pytest.fixture(params=[1, 2, 3])
def setup(request):
    """each param is called, overall three times,
     u can take param values using request context"""
    ret_val = request.param
    print("\nSetup! ret_val = {}".format(ret_val))
    return ret_val


def test1(setup):
    print("\nsetup = {}".format(setup))
    assert True
