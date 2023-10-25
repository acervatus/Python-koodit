import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinennopeus = 0, kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinennopeus = nykyinennopeus
        self.kuljettumatka = kuljettumatka
    def kiihdyta(self, maara):
        self.nykyinennopeus += maara
        if self.nykyinennopeus < 0:
            self.nykyinennopeus = 0
        elif self.nykyinennopeus > self.huippunopeus:
            self.nykyinennopeus = self.huippunopeus
    def kulje(self, tuntimaara):
        self.kuljettumatka += int(self.nykyinennopeus * tuntimaara)

autolista = []
for i in range(10):
    autolista.append(Auto("ABC-" + str(i + 1), random.randint(100, 200)))
while max(u.kuljettumatka for u in autolista) < 10000:
    for i in autolista:
        i.kiihdyta(random.randint(-10, 15))
        i.kulje(1.0)
for e in autolista:
    print(e.rekisteritunnus)
    print("Huippunopeus: " + str(e.huippunopeus) + " km/h")
    print("Nykyinen nopeus: " + str(e.nykyinennopeus) + " km/h")
    print("Kuljettu matka: " + str(e.kuljettumatka) + " km/h")
    print(" ")
