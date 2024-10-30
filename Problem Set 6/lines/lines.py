import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    file = open(sys.argv[1], "r")

    lines = file.readlines()

    total_lines = 0

    for line in lines:
        if line.strip() != "" and not line.strip().startswith("#"):
            total_lines += 1

    print(total_lines)
except FileNotFoundError:
    sys.exit("File does not exist.")
