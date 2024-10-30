import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)

    if match:
        start_time = standardise(match.group(1), match.group(2), match.group(3))
        end_time = standardise(match.group(4), match.group(5), match.group(6))

        return f"{start_time} to {end_time}"
    else:
        raise ValueError


def standardise(hour, minute, part):
    if hour == "12":
        if part == "AM":
            hour = "00"
    else:
        if part == "AM":
            hour = f"{int(hour):02}"
        else:
            hour = f"{int(hour) + 12}"

    if minute == None:
        minute = "00"
    else:
        minute = f"{int(minute):02}"

    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
