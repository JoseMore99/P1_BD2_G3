import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/otros/ability_all.csv')

# Acceder a las columnas por nombre
abilities = data['ability']
games = data['game']
descriptions = data['Description']
games= games.apply(ast.literal_eval)
anterior=""
for i in range(len(abilities)):
    #print(f"Ability: {abilities.iloc[i]}")
    #print(f"game: {games.iloc[i]}")
    if anterior==abilities.iloc[i]:
        continue
    else:
        db.query_con_retorno("""INSERT INTO poke_g3.ability(name)VALUES(%s);""", (abilities.iloc[i]))
        anterior=abilities.iloc[i]
    #for j in games.iloc[i]:
       # print(j)
    #print(f"Description: {descriptions.iloc[i]}")
    #print('-' * 20)  