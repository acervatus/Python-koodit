lentoasema = {"EFHK":"Helsinki-Vantaan lentoasema"}
while True:
    valinta = input("Uusi lentoasema, hae lentoasema tai lopeta(u/h/l): ")
    if valinta == "u":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasema[koodi] = nimi
    elif valinta == "h":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        print(lentoasema[koodi])
    elif valinta == "l":
        break
