import addition
import pytest

def test_add():
    assert True #one test
    assert addition.add(4, 5) == 9 #another test within same function

def test_sub():
    pass # passes this test


#to test, write:  python3 -m pytest addition_test.py