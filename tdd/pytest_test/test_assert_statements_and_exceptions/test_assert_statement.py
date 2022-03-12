from pytest import approx


def test_int_assert():
    assert 1 == 1


def test_str_assert():
    assert "str" == "str"


def test_float_assert():
    assert 1.0 == 1.0


def test_array_assert():
    assert [1, "D", 3] == [1, "D", 3]


def test_dict_assert():
    assert {"1": 1} == {"1": 1}


def test_float():
    """ assert (0.1 + 0.2) == 0.3 this will return error,
    so we use approx module,
    we can use approx in either side"""
    assert approx(0.1 + 0.2) == 0.3

