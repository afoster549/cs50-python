from tabulate import tabulate
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    file = open(sys.argv[1], "r")

    lines = file.readlines()

    head = []
    table = []

    for i in range(0, len(lines)):
        line = lines[i].strip()

        if i == 0:
            head = line.split(",")
        else:
            table.append(line.split(","))

    print(tabulate(table, headers=head, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist.")
