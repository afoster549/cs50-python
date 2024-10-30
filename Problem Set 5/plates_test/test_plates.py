from plates import is_valid

def main():
    test_plates()

def test_plates():
    assert is_valid("AA") == True
    assert is_valid("A2") == False

    assert is_valid("2A") == False
    assert is_valid("22") == False

    assert is_valid("A") == False

    assert is_valid("AA0") == False
    assert is_valid("AA1A") == False
    assert is_valid("AA11") == True

    assert is_valid("PI3.14") == False

if __name__ == "__main__":
    main()
