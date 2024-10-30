import pytest
from um import count

def test():
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("Um...") == 1
    assert count("yum") == 0
