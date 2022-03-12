import pytest
from checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    return checkout


# def test_can_add_item_price(checkout):
#     """Tests if price can be added to the item"""
#     checkout.add_item_price("a", 4)
#
#
# def test_can_add_item(checkout):
#     """Tests if item can be added"""
#     checkout.add_item("a")


def test_can_calculate_total(checkout):
    """Test if checkout class can calculate total"""
    checkout.add_item_price("a", 50)
    checkout.add_item("a")
    assert checkout.calculate_total() == 50


def test_get_correct_total_with_multiple_items(checkout):
    """Tests if sum of all product price is correct"""
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 3


def test_can_add_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)


def test_can_apply_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    assert checkout.calculate_total() == 2


def test_exception_with_bad_item(checkout):
    with pytest.raises(Exception):
        checkout.add_item("c")
