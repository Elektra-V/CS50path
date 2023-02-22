import pytest
from jar import Jar


def test_init():
   
    cookie_jar = Jar(9000, 8999)
    assert cookie_jar.capacity == 9000
    assert cookie_jar.size == 8999

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_capacity():

    chocolate_cookie_jar = Jar()
    crunchy_cookie_jar = Jar(10)

    assert crunchy_cookie_jar.capacity == 10
    assert chocolate_cookie_jar.capacity == 12

    # Check that Jar capacity can not be manually instantiated with negative integer values.
    with pytest.raises(ValueError):
        double_fudge_brownies = Jar(-1)

    with pytest.raises(ValueError):
        double_fudge_brownies = Jar("dog")


def test_size():

    choco_chip_jar = Jar()
    oatmeal_jar = Jar()

    assert choco_chip_jar.size == 0
    assert oatmeal_jar.size == 0

    # Check that Jar size can not be manually instantiated with negative integer values.
    with pytest.raises(ValueError):
        caramel_jar = Jar(12, -1)


def test_deposit():
    
    choco_chip_jar = Jar(10)
    choco_chip_jar.deposit(4)

    assert  choco_chip_jar.size == 4

    oatmeal_jar = Jar(12, 11)
    with pytest.raises(ValueError):
        oatmeal_jar.deposit(2)


def test_withdraw():
   
    fudge_cookie_jar = Jar(4)
    fudge_cookie_jar.deposit(3)
    fudge_cookie_jar.withdraw(2)

    assert fudge_cookie_jar.size == 1

    oatmeal_jar = Jar(12, 11)
    with pytest.raises(ValueError):
        oatmeal_jar.withdraw(12)


def test_str():
    
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪"


def test_capacity_property():
    
    coconut_jar = Jar(24)
    assert coconut_jar.capacity == 24


def test_size_property():

    coconut_jar = Jar(32)
    coconut_jar.deposit(32)
    coconut_jar.withdraw(12)
    assert coconut_jar.size == 20