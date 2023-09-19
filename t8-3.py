def Matka(koodi1:str, koodi2:str):
    sql = "SELECT latitude_deg, longitude_deg FROM airports WHERE ident ='" + koodi1 + "' OR ident ='" + koodi2 + "'"
    haku = yhteys.cursor()
    haku.execute(sql)
    tulos = haku.fetchall()
    if len(tulos) > 1:
        paikka1 = (tulos[0][0], tulos[0][1])
        paikka2 = (tulos[1][0], tulos[1][1])
        print(great_circle(paikka1, paikka2))

from geopy.distance import great_circle
import mysql.connector
yhteys = mysql.connector.connect(host='127.0.0.1',port= 3306,user='root',password='Qwerty',database="Lentokenttatietokanta", autocommit=True)
icao1 = input("Anna lentokentän 1 ICAO-koodi: ")
icao2 = input("Anna lentokentän 2 ICAO-koodi: ")
Matka(icao1, icao2)