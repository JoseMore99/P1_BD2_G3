import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemons_2.csv')

# pokedex_number,name,types
pokedex_number = data['name']
types = data['types']
types= types.apply(ast.literal_eval)
anterior=""
for i in range(len(pokedex_number)):
    for j in types.iloc[i]:
        db.query_con_retorno("""INSERT INTO poke_g3.pokemon_type
( pokemon_id, type_id)
VALUES((SELECT id FROM poke_g3.pokemon WHERE name = %s ),(SELECT id FROM poke_g3.types WHERE name = %s));""", (pokedex_number.iloc[i],j))