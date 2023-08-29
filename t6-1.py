import random
def Noppa():
    return random.randrange(1,7)



if __name__ == "__main__":
    while True:
        luku = Noppa()
        print(luku)
        if luku == 6:
            break