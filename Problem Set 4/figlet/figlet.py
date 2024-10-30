import sys
from pyfiglet import Figlet

figlet = Figlet()

try:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font" or sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        message = input("Input: ")

        figlet.setFont(font = sys.argv[2])

        print(figlet.renderText(message))
except IndexError:
    sys.exit("Invalid usage")
