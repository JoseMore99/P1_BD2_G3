import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/Breeding.csv')

# pokedex_id,Egg_groups
pokedex_number = data['pokedex_id']
Egg_groups = data['Egg_groups']
Egg_groups= Egg_groups.apply(ast.literal_eval)
anterior=""
for i in range(len(pokedex_number)):
    for j in Egg_groups.iloc[i]:
        db.query_con_retorno("""INSERT INTO poke_g3.egg_groups_breeding
(breeding_id, egg_group_id)
VALUES((SELECT id FROM poke_g3.breeding WHERE pokemon_id =(SELECT id FROM poke_g3.pokemon WHERE pokedex_id = %s LIMIT 1) LIMIT 1),(SELECT id FROM poke_g3.egg_groups WHERE name = %s));""", (int(pokedex_number.iloc[i]),j))