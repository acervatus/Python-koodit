kuhanpituus = int(input("Anna kuhan pituus senttimetreinä: "))
if kuhanpituus < 37:
    print("Laske kuha takaisin, se on " + str(37 - kuhanpituus) + " cm liian pieni alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuhan saa viedä kotiin.")
