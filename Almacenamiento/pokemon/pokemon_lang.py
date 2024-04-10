import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_languages.csv')

# Evolving_from,Evolving_to,level,item,description,type
pokedex_id = data['pokedex_id']
language = data['language']
name = data['name']
for i in range(len(pokedex_id)):
        db.query_con_retorno("""INSERT INTO poke_g3.pokemon_language
(pokemon_id, language_id, name)
VALUES((SELECT id FROM poke_g3.pokemon WHERE pokedex_id = %s LIMIT 1), (SELECT id FROM poke_g3.languages WHERE name = %s), %s);""",
    (int(pokedex_id.iloc[i]),language.iloc[i],name.iloc[i]))