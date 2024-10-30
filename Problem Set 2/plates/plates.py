def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        numeric = False

        if not s[:2].isalpha():
            return False

        for i in range(0, len(s)):
            if s[i].isnumeric():
                if s[i] == "0" and not numeric:
                    return False

                numeric = True
            elif s[i].isalpha() and numeric:
                return False
            elif s[i].isalpha():
                continue
            else:
                return False

        return True
    else:
        return False
main()
