from bank import value

def test_hello():
    assert value("Hello") == "$0"
    assert value("Hello, Newman") == "$0"

def test_h():
    assert value("How you doing?") == "$20"

def test_no_h():
    assert value("What's happening?") == "$100"