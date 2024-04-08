import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/otros/items.csv')

# Acceder a las columnas por nombre
name = data['name']
efect = data['effect']
cat = data['cathegory']
for i in range(len(name)):
    #print(f"Ability: {name.iloc[i]}")
    #print(f"game: {games.iloc[i]}")
    print( "valor"+str(cat.iloc[i]))
    if  str(efect.iloc[i])=="nan":
            db.query("""INSERT INTO poke_g3.item
    (name,effect,category)
    VALUES(%s,' ',(SELECT id FROM poke_g3.item_category WHERE name = %s));""", 
    (name.iloc[i],cat.iloc[i]))
    elif str(cat.iloc[i])=="nan":
        db.query("""INSERT INTO poke_g3.item
(name,effect,category)
VALUES(%s,%s,%s);""", 
(name.iloc[i],efect.iloc[i],-1))
    else:
        db.query("""INSERT INTO poke_g3.item
(name,effect,category)
VALUES(%s,%s,(SELECT id FROM poke_g3.item_category WHERE name = %s));""", 
(name.iloc[i],efect.iloc[i],cat.iloc[i]))