import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemons_2.csv')

# pokedex_number,name,types,total,hp,attack,defense,special_attack,special_defense,speed,total
name = data['name']
hp = data['hp']
attack = data['attack']
defense = data['defense']
special_attack = data['special_attack']
special_defense = data['special_defense']
speed = data['speed']
total = data['total']
for i in range(len(name)):
        print()
        db.query_con_retorno("""INSERT INTO poke_g3.pokemon_basic_stats
( pokemon_id, hp, attack, defense, special_attack, special_defense, speed, total)
VALUES((SELECT id FROM poke_g3.pokemon WHERE name = %s ),%s,%s,%s,%s,%s,%s,%s);""",
 (name.iloc[i],hp.iloc[i],attack.iloc[i],defense.iloc[i],special_attack.iloc[i],special_defense.iloc[i],speed.iloc[i],total.iloc[i]))