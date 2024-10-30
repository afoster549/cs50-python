while True:
    ammount = input("Fraction: ")

    try:
        x, y = ammount.split("/")

        x = int(x)
        y = int(y)

        if x <= y:
            percent = round((x / y) * 100)

            if percent >= 99:
                print("F")
            elif percent <= 1:
                print("E")
            else:
                print(f"{percent}%")

            break
    except:
        pass
