items = {}

while True:
    try:
        item = input()

        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        for item in sorted(items):
            print(f"{items[item]} {item.upper()}")

        break
