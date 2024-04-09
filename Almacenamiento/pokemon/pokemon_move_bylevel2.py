import db
import csv

with open('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_move_bylevel.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for indice, f in enumerate(lector_csv):
        if indice == 0:
            continue
        print(f)
        db.query("""INSERT INTO poke_g3.pokemon_moves_bylevel
(pokemon_id, move_id, level)
VALUES((SELECT id FROM poke_g3.pokemon WHERE pokedex_id = %s LIMIT 1),(SELECT id FROM poke_g3.move WHERE name = %s),%s);""", 
(f[0],f[1],f[2]))