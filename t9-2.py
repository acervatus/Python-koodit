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

auto = Auto("ABC-123", 142)
print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.nykyinennopeus)
print(auto.kuljettumatka)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(auto.nykyinennopeus)
auto.kiihdyta(-200)
print(auto.nykyinennopeus)