class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinennopeus = 0, kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinennopeus = nykyinennopeus
        self.kuljettumatka = kuljettumatka

auto = Auto("ABC-123", 142)
print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.nykyinennopeus)
print(auto.kuljettumatka)