lista = []
while True:
    lisaa = input("Anna luku: ")
    if lisaa == "":
        break
    else:
        lista.append(int(lisaa))
lista.sort(reverse=True)
for i in range(5):
    print(lista[i])