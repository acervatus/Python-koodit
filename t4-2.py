while True:
    tuumat = float(input("Anna negatiivinen tuumamäärä: "))
    if tuumat >= 0:
        break
    print(str(tuumat * 2.54) + " cm")