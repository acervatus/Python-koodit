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
class Talo:
    def __init__(self, alinkerros, ylinkerros, hissienmaara):
        self.hissienmaara = hissienmaara
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.hissit = []
        for i in range(self.hissienmaara):
            self.hissit.append(Hissi(self.alinkerros, self.ylinkerros))
    def aja_hissiä(self, hissinnumero, kohdekerros):
        self.hissit[hissinnumero - 1].siirry_kerrokseen(kohdekerros)
    def palohälytys(self):
        for i in self.hissit:
            i.siirry_kerrokseen(self.alinkerros)
            
hissi = Hissi(1, 5)
hissi.siirry_kerrokseen(3)
hissi.siirry_kerrokseen(hissi.alinkerros)
talo = Talo(1, 6, 4)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(1, 2)
talo.aja_hissiä(1, 4)
talo.aja_hissiä(1, 1)
talo.palohälytys()