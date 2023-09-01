def MuutaGallonat(maara:float):
    return maara * 3.785
if __name__ == "__main__":
    while True:
        gallona = float(input("Anna gallonamäärä: "))
        if gallona < 0:
            break
        else:
            print(str(MuutaGallonat(gallona)) + " Litraa")
