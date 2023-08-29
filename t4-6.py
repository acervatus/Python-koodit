import random
pisteet = int(input("Arvottavat pisteet: "))
monta = 0
for i in range(pisteet):
    x = random.randrange(-100, 101) / 100.0
    y = random.randrange(-100, 101) / 100.0
    if x * x + y * y < 1.0:
        monta += 1
print(str(4.0 * monta / pisteet))