import pytest

from FizzBuzz import fizz_buzz


def check_fizz_buzz(value, expected_value):
    ret_val = fizz_buzz(value)
    assert ret_val == expected_value


def test_returns_1_with_1_passed_in():
    check_fizz_buzz(1, "1")


def test_returns_2_with_2_passed_in():
    check_fizz_buzz(2, "2")


def test_returns_fizz_with_3_passed_in():
    check_fizz_buzz(3, "Fizz")


def test_returns_buzz_with_5_passed_in():
    check_fizz_buzz(5, "Buzz")


def test_returns_fuzz_with_6_passed_in():
    check_fizz_buzz(6, "Fizz")


def test_returns_buzz_with_10_passed_in():
    check_fizz_buzz(10, "Buzz")


def test_test_fizz_buzz_with_15_passed_in():
    check_fizz_buzz(15, "FizzBuzz")
