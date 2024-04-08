
import db
import csv

u=db.query_con_retorno("SELECT * FROM ayd.Users WHERE idUser = %s", (1,))
print(u)
with open('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_indi.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for indice, f in enumerate(lector_csv):
        if indice == 0:
            continue
        db.query("""INSERT INTO poke_g3.pokemon
(pokedex_id, name, especie, height, weight, id_nature)
VALUES( %s, %s, %s, %s, %s, %s);""", 
(f[0],f[1],f[2],f[3],f[4],1))