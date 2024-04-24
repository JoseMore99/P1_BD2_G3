import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_ability.csv')

#pokedex_id,abilities
pokedex_id = data['pokedex_id']
abilities = data['abilities']
abilities= abilities.apply(ast.literal_eval)
for i in range(len(pokedex_id)):
    for j in abilities.iloc[i]:
            db.query_con_retorno("""INSERT INTO poke_g3.pokemon_ability
    (pokemon_id, ability_id)
    VALUES((SELECT id FROM poke_g3.pokemon WHERE pokedex_id = %s LIMIT 1),(SELECT id FROM poke_g3.ability WHERE name = %s  LIMIT 1));""", (int(pokedex_id.iloc[i]),j))