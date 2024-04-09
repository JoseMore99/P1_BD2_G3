
import db
import csv

with open('J:/universidad/bases 2/P1_BD2_G3/otros/eggGroups.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for indice, f in enumerate(lector_csv):
        if indice == 0:
            continue
        db.query("""INSERT INTO poke_g3.egg_groups
(name)
VALUES(%s);""", 
(f[0]))