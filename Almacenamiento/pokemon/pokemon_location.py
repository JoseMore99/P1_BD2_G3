import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_location.csv')

# pokedex_id,game,location 
pokedex_id = data['pokedex_id']
game = data['game']
location = data['location']
game= game.apply(ast.literal_eval)
for i in range(len(pokedex_id)):
    for j in game.iloc[i]:
        lugar = str(location.iloc[i]).split(", ")
        for k in lugar:
            place=k
            if k.isdigit():
                place = "Route "+place
            db.query_con_retorno("""INSERT INTO poke_g3.pokemon_location
    (pokemon_id, location_id)
    VALUES((SELECT id FROM poke_g3.pokemon WHERE pokedex_id = %s LIMIT 1),
        (SELECT id FROM poke_g3.location WHERE location = %s  AND gen_games_id = (SELECT id FROM poke_g3.gen_games WHERE name = %s) LIMIT 1));""", (int(pokedex_id.iloc[i]),place,j))
