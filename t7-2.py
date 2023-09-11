nimet = set()
while True:
    lisaa = input("Anna nimi: ")
    if lisaa != "":
        if nimet.__contains__(lisaa):
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
        nimet.add(lisaa)
    else:
        break
for i in nimet:
    print(i)