def KarsiLista(listakarsi:[]):
    return [i for i in listakarsi if i % 2 == 0]

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(str(lista) + " --> " + str(KarsiLista(lista)))