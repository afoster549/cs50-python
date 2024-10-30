camelCase = input("camelCase: ")
snakeCase = ""

for char in camelCase:
    if char.isupper():
        snakeCase += "_" + char.lower()
    else:
        snakeCase += char

print("snake_case:", snakeCase)
