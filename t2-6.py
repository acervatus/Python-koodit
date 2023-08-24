import random
kolmi = ""
nelja = ""
for i in range(3):
    kolmi += str(random.randint(0, 9))
for i in range(4):
    nelja += str(random.randint(1, 6))
print(kolmi + "\n" + nelja)