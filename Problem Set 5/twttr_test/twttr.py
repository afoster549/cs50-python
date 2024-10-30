def main():
    print(shorten(input("Input: ")))

def shorten(word):
    removed = ""

    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            removed += char

    return removed


if __name__ == "__main__":
    main()
