from numb3rs import validate

def main():
    test_valid()
    test_invalid()

def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.0.1") == True

def test_invalid():
    assert validate("65.0.-54.1") == False
    assert validate("275.0.65.7") == False
    assert validate("127.999.999.999") == False
    assert validate("cat") == False

if __name__ == "__main__":
    main()
