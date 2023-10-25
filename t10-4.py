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
class Kilpailu:
    def __init__(self, kilpailunnimi, pituus, osallistuvatautot):
        self.kilpailunimi = kilpailunnimi
        self.pituus = pituus
        self.osallistuvatautot = osallistuvatautot
    def tunti_kuluu(self):
        for i in self.osallistuvatautot:
            i.kiihdyta(random.randint(-10, 15))
            i.kulje(1.0)
    def tulosta_tilanne(self):
        print(self.kilpailunimi)
        print("------------------")
        for e in self.osallistuvatautot:
            print(e.rekisteritunnus)
            print("Huippunopeus: " + str(e.huippunopeus) + " km/h")
            print("Nykyinen nopeus: " + str(e.nykyinennopeus) + " km/h")
            print("Kuljettu matka: " + str(e.kuljettumatka) + " km/h")
            print(" ")
    def kilpailu_ohi(self):
        if max(u.kuljettumatka for u in autolista) >= self.pituus:
            return True
        else:
            return False
autolista = []
for i in range(10):
    autolista.append(Auto("ABC-" + str(i + 1), random.randint(100, 200)))
kilpailu = Kilpailu("Suuri romuralli.", 8000, autolista)
tunnit = 0
while kilpailu.kilpailu_ohi() != True:
    tunnit += 1
    kilpailu.tunti_kuluu()
    if kilpailu.kilpailu_ohi() == True:
        kilpailu.tulosta_tilanne()
    if tunnit == 10:
        tunnit = 0
        kilpailu.tulosta_tilanne()