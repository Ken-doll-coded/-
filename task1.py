with open("quotes.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)


at = input("ti semga")
with open("quotes.txt", "a")as file:
    file.write(f"({at})")

while True:
    aw = input("citata(da/net)")
    aw = aw.lower()
    if aw == "da":
        qo = input("vedi citaty")
        at = input("vedi citaty")
        file = open("quotes.txt", "a")
        file.write(f"{qo}\n({au}\\n")
        file.close()
    else:
        break

with open