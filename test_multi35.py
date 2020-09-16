#!/usr/bin/python3
# multiples of 3 and 5 project Euler
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
import pytest
import multi35

def test_below_10():
    result = multi35.multiples(10)
    assert result == 23


def test_max_1000():
    result = multi35.multiples(1000)
    assert result == 233168