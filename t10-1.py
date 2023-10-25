class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = 0
    def siirry_kerrokseen(self, liiku):
        if liiku < self.kerros:
            while self.kerros > liiku:
                self.kerros_alas()
        else:
            while self.kerros < liiku:
                self.kerros_ylös()
    def kerros_ylös(self):
        self.kerros += 1
        print("Kerros on: " + str(self.kerros))
    def kerros_alas(self):
        self.kerros -= 1
        print("Kerros on: " + str(self.kerros))

hissi = Hissi(1, 5)
hissi.siirry_kerrokseen(3)
hissi.siirry_kerrokseen(hissi.alinkerros)
