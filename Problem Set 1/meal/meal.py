def main():
    time = convert(input("What time is it? "))

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hour, min = time.split(":")

    return int(hour) + (int(min) / 60)

if __name__ == "__main__":
    main()
