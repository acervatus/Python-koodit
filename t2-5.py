leiviskat = float(input("Anna leiviskät. "))
naulat = float(input("Anna naulat. "))
luodit = float(input("Anna luodit. "))
massa = luodit * 13.3 + naulat * 13.3 * 32 + leiviskat * 13.3 * 32 * 20
print("Massa nykymittojen mukaan: \n" + str(int(massa // 1000)) + " kilogrammaa ja " + str(format(massa % 1000, '.2f')) + " grammaa.")