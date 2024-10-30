import os
import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[2].split(".")[1] not in ["png", "jpg", "jpeg"]:
        sys.exit("Invalid output")
    elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Input and output have different extensions")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Input does not exist")

    before = Image.open(sys.argv[1], "r")
    shirt = Image.open("shirt.png")

    before = ImageOps.fit(before, shirt.size)

    before.paste(shirt, shirt)

    before.save(sys.argv[2])

if __name__ == "__main__":
    main()
