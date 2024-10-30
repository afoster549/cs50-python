import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

with open(sys.argv[1], newline="") as before_csv:
    csv_reader = csv.reader(before_csv, delimiter=" ", quotechar='"')

    for row in csv_reader:
        print(", ".join(row))
