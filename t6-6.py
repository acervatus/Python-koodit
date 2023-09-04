import math
def PizzaLaske(halkaisija, hinta):
    return 1000.0 / (math.pi * (halkaisija / 2)**2) * hinta

if __name__ == "__main__":
    pizzahalkaisija = float(input("Anna pizzan halkaisija senttimetreinä: "))
    pizzahinta = float(input("Anna pizzan hinta euroina: "))
    pizzahalkaisija2 = float(input("Anna pizzan 2 halkaisija senttimetreinä: "))
    pizzahinta2 = float(input("Anna pizzan 2 hinta euroina: "))
    if PizzaLaske(pizzahalkaisija, pizzahinta) < PizzaLaske(pizzahalkaisija2, pizzahinta2):
        print("Ensimmäisellä pizzalla on parempi yksikköhinta.")
    elif PizzaLaske(pizzahalkaisija, pizzahinta) > PizzaLaske(pizzahalkaisija2, pizzahinta2):
        print("Toisella pizzalla on parempi yksikköhinta")
    else:
        print("Pizzoilla on sama yksikköhinta.")
