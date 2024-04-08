import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/otros/gen_games.csv')

# Acceder a las columnas por nombre
name = data['name']
generation = data['generation']
region = data['region']
for i in range(len(name)):

    db.query("""INSERT INTO poke_g3.gen_games
(generation, name, region)
VALUES(%s, %s, %s);""", 
(generation.iloc[i],name.iloc[i],region.iloc[i]))