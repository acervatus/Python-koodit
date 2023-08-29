luku = int(input("Anna luku: "))
alkuluku = True
for i in range(2, luku):
    if luku / i == int(luku / i):
        alkuluku = False
if alkuluku == True:
    print("On alkuluku")
else:
    print("Ei ole alkuluku")
