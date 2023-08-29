import random
numero = random.randrange(1, 11)
while True:
    arvaus = int(input("Anna arvaus: "))
    if arvaus < numero:
        print("Liian pieni arvaus")
    elif arvaus > numero:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break