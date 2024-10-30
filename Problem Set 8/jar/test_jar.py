import pytest
from jar import Jar

def test_init():
    jar = Jar(8)
    assert jar.capacity == 8


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0

    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(8)


def test_withdraw():
    jar = Jar()
    jar.deposit(8)

    jar.withdraw(4)
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.withdraw(6)
