import random
lukumaara = int(input("Arpakuutioiden lukumäärä: "))
summa = 0
for i in range(lukumaara):
    summa += random.randrange(1, 7)
print("Arpakuutioiden summa: " + str(summa))