import sys
import requests

ammount_bitcoin = 0

try:
    ammount_bitcoin = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    one_bitcoin = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))

    amount = one_bitcoin * ammount_bitcoin

    print(f"${amount:,.4f}")
except requests.RequestException:
    print("Something went wrong!")
