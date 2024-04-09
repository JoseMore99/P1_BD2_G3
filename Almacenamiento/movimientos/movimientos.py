import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/movimientos/moviminetos9.csv')

# name,types,power,Category,acc,pp,efect
name = data['name']
types = data['types']
power = data['power']
Category = data['Category']
acc = data['acc']
pp = data['pp']
efect = data['efect']
for i in range(len(name)):
    efecto =""
    poder=-1
    acur=-1
    pi=-1
    Categ="singular"
    tipo="nulo"
    if  str(efect.iloc[i])!="nan":
           efecto =efect.iloc[i]
    if  str(power.iloc[i])!="—":
           poder =power.iloc[i]
    if  str(acc.iloc[i])!="—":
           acur =acc.iloc[i]
    if  str(pp.iloc[i])!="—":
           pi =pp.iloc[i]
    if  str(Category.iloc[i])!="nan":
           Categ =Category.iloc[i]
    
    if  str(types.iloc[i])!="nan":
           tipo =types.iloc[i]
    
    db.query("""INSERT INTO poke_g3.move
    (name, type, move_category, power, accuracy, effect)
VALUES(%s,(SELECT id FROM poke_g3.types WHERE name = %s),(SELECT id FROM poke_g3.move_categories WHERE name = %s),%s,%s,%s);""", 
(name.iloc[i],tipo,Categ,poder,acur,efecto))