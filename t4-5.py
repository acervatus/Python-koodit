nimi = "python"
salasana = "rules"
yritykset = 0
while yritykset < 5:
    ynimi = input("Anna käyttäjätunnus: ")
    ysalasana = input("Anna salasana: ")
    if ynimi != nimi or ysalasana != salasana:
        yritykset += 1
        if yritykset == 5:
            print("Pääsy evätty")
            break
        else:
            print("Yritä uudelleen")
    else:
        print("Tervetuloa")
        break