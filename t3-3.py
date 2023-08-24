sukupuoli = input("Anna biologinen sukupuoli(m, n): ")
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "m":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "n":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
