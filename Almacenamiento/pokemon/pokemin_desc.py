import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_desc.csv')

pokedex_id = data['pokedex_id']
games = data['game']
descriptions = data['description']
games= games.apply(ast.literal_eval)
for i in range(len(pokedex_id)):
    for j in games.iloc[i]:
        db.query_con_retorno("""INSERT INTO poke_g3.pokemon_desc_gen_games
(gen_game_id, pokemon_id, description)
                             VALUES((SELECT id FROM poke_g3.gen_games WHERE name = %s),(SELECT id FROM poke_g3.pokemon WHERE  pokedex_id = %s LIMIT 1),%s);""", 
                             (j,int(pokedex_id.iloc[i]),descriptions.iloc[i]))