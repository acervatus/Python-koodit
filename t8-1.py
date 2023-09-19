def HaeKoodilla(icaokoodi:str):
    sql = "SELECT name, municipality FROM airports WHERE ident ='" + icaokoodi + "'"
    haku = yhteys.cursor()
    haku.execute(sql)
    tulos = haku.fetchall()
    if len(tulos) > 0:
        print(str(tulos[0][0]) + ", " + str(tulos[0][1]))
import mysql.connector
yhteys = mysql.connector.connect(host='127.0.0.1',port= 3306,user='root',password='Qwerty',database="Lentokenttatietokanta", autocommit=True)
HaeKoodilla(input("Anna icao-koodi: "))