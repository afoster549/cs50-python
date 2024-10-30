from datetime import date
import inflect
import sys
import re


def main():
    s = input("Date of Birth ")

    minutes = get_minutes(s)

    print(minutes)

def get_minutes(s):
    if search := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", s):
        s = list(search.groups())
    else:
        sys.exit("Invalid date")

    d = convert_and_check(s)

    today = date.today()

    birthday = date(d[0], d[1], d[2])

    diff = birthday - today

    no_days = -int(diff.days)

    minutes = no_days * 24 * 60

    engine = inflect.engine()

    minutes_words = engine.number_to_words(minutes)

    minutes_words = minutes_words.replace(" and", "").capitalize()

    return minutes_words + " minutes"

def convert_and_check(d):
    d = list(map(int, d))

    if d[1] < 0 or d[1] > 12:
        sys.exit("Invalid date")
    elif d[2] < 0 or d[2] > 31:
        sys.exit("Invalid date")

    return d

if __name__ == "__main__":
    main()
