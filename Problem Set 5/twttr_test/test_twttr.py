from twttr import shorten

def main():
    test_strings()
    test_numbers()

def test_strings():
    assert shorten("a") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"

    assert shorten("CS50") == "CS50"
    assert shorten("d,A!:") == "d,!:"

if __name__ == "__main__":
    main()
