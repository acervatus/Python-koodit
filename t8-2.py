def etsimaasta(maakoodi:str):
    sql = "SELECT type FROM airports WHERE iso_country ='" + maakoodi + "'"
    haku = yhteys.cursor()
    haku.execute(sql)
    tulos = haku.fetchall()
    for i in set(tulos):
        print(i[0] + ": " + str(tulos.count(i)))
        
import mysql.connector
yhteys = mysql.connector.connect(host='127.0.0.1',port= 3306,user='root',password='Qwerty',database="Lentokenttatietokanta", autocommit=True)
etsimaasta(input("Anna maakoodi: "))