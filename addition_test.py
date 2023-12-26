import addition
import pytest

def test_add():
    assert addition.add(4, 5) == 10

def test_sub():
    pass


#to test, write:  python3 -m pytest addition_test.py