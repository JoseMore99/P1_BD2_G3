import db
import csv

with open('J:/universidad/bases 2/P1_BD2_G3/otros/locations.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for indice, f in enumerate(lector_csv):
        if indice == 0:
            continue
        ids =  db.query_con_retorno("""SELECT id FROM poke_g3.gen_games WHERE generation = %s;""",(f[1]) )
        for i in ids:

            db.query("""INSERT INTO poke_g3.location
    (gen_games_id,location)
    VALUES(%s,%s);""", 
(i,f[0]))