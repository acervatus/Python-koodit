lista = []
while True:
    sisaan = input("Anna luku: ")
    if sisaan != "":
        lista.append(int(sisaan))
    else:
        break
print("Pienin luku: " + str(min(lista)))
print("Suurin luku: " + str(max(lista)))