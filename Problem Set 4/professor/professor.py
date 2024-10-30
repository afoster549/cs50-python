from random import randint

def main():
    level = get_level()
    score = 0
    question_number = 0

    while question_number < 10:
        attempt = 0

        x, y = generate_integer(level), generate_integer(level)

        while attempt < 3:
            try:
                ans = int(input(f"{x} + {y} = "))

                if ans == x + y:
                    score += 1

                    break
                else:
                    print("EEE")

                    attempt += 1
            except:
                print("EEE")

                attempt += 1

        print(f"{x} + {y} = {x + y}")

        question_number += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level < 1 or level > 3:
                raise ValueError
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)

if __name__ == "__main__":
    main()
