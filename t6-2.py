import random
def Noppa(tahkoja:int):
    return random.randrange(1,tahkoja+1)

if __name__ == "__main__":
    tahkomaara = int(input("Anna nopan tahkomäärä: "))
    while True:
        luku = Noppa(tahkomaara)
        print(luku)
        if luku == tahkomaara:
            break