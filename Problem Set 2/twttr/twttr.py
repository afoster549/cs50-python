text = input("Input: ")

removed = ""

for char in text:
    if char.lower() not in ["a", "e", "i", "o", "u"]:
        removed += char

print(removed)
