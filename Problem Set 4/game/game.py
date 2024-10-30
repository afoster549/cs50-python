from random import randint

level = 0

while True:
    try:
        level = int(input("Level: "))

        if level > 0:
            break
    except:
        pass

num = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess > num:
            print("Too large!")
        elif guess < num:
            print("Too small!")
        else:
            print("Just right!")

            break
    except:
        pass
