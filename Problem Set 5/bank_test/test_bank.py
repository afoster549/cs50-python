from bank import value

def main():
    test_greetings()

def test_greetings():
    assert value("Hello, how are you?") == 0

    assert value("Hey, how are you?") == 20

    assert value("Good morning.") == 100

if __name__ == "__main__":
    main()
