import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/otros/ability_all.csv')

# Acceder a las columnas por nombre
name = data['ability']
games = data['game']
descriptions = data['Description']
games= games.apply(ast.literal_eval)
for i in range(len(name)):
    for j in games.iloc[i]:
        db.query_con_retorno("""INSERT INTO poke_g3.ability_desc_gen_games(gen_game_id,ability_id,description)
                             VALUES((SELECT id FROM poke_g3.gen_games WHERE name = %s),(SELECT id FROM poke_g3.ability WHERE name = %s),%s);""", 
                             (j,name.iloc[i],descriptions.iloc[i]))