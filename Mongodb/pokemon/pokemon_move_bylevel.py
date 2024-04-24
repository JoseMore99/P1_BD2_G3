import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_move_bylevel.csv')

# pokedex_id,move_name,level
pokedex_id = data['pokedex_id']
move_name = data['move_name']
level = data['level']
for i in range(len(pokedex_id)):
    db.query("""INSERT INTO poke_g3.pokemon_moves_bylevel
(pokemon_id, move_id, level)
VALUES((SELECT id FROM poke_g3.pokemon WHERE pokedex_id = %s LIMIT 1),(SELECT id FROM poke_g3.move WHERE name = %s),%s);""", 
(pokedex_id.iloc[i],move_name.iloc[i],level.iloc[i]))