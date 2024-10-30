import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")

        names.append(name)
    except EOFError:
        break

names = tuple(names)

print("\nAdieu, adieu, to", p.join(names))
