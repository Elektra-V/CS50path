from plates import is_valid

def test_two_letters():
    assert is_valid('CS50') == True


def test_middle_zero():
    assert is_valid('CS05') == False


def test_num_end():
    assert is_valid('CS50P') == False


def test_periods():
    assert is_valid('PI3.4') == False


def test_spaces_commas():
    assert is_valid('Hello, World') == False


def test_just_nums():
    assert is_valid('50') == False


def test_just_chars():
    assert is_valid('OUTATIME') == False