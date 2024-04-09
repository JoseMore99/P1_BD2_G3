import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/Training.csv')

#pokedex_id,EV_yield,catch_rate,base_friendship,base_exp,growth_rate cles
pokedex_id = data['pokedex_id']
EV_yield = data['EV_yield']
catch_rate = data['catch_rate']
base_friendship = data['base_friendship']
base_exp = data['base_exp']
growth_rate = data['growth_rate']
for i in range(len(pokedex_id)):
    catch=catch_rate.iloc[i].split(" ")
    if base_friendship.iloc[i]=="—":
        db.query("""INSERT INTO poke_g3.training
    (pokemon_id, ev_yield, catch_rate, base_friendship, base_exp, growth_rate)
    VALUES((SELECT id FROM poke_g3.pokemon WHERE  pokedex_id = %s LIMIT 1),%s,%s,%s,%s,%s);""", 
    (int(pokedex_id.iloc[i]),EV_yield.iloc[i],catch[0],'-1',-1,growth_rate.iloc[i]))
    