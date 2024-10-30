months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if len(date.split("/")) == 3:
            date = date.split("/")

            if int(date[1]) <= 31 and int(date[0]) <= 12:
                print(f"{int(date[2]):04}-{int(date[0]):02}-{int(date[1]):02}")

                break
        else:
            date = date.split(" ")
            date[1] = date[1][:-1]

            if date[0] in months and int(date[1]) <= 31:
                 print(f"{int(date[2]):04}-{int(months.index(date[0]) + 1):02}-{int(date[1]):02}")

                 break
    except:
        pass
