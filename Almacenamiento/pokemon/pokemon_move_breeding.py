import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/Breeding.csv')

# pokedex_id,Egg_groups,gender_male ,gender_female ,egg_cycles
pokedex_id = data['pokedex_id']
gender_male = data['gender_male']
gender_female = data['gender_female']
egg_cycles = data['egg_cycles']
for i in range(len(pokedex_id)):
    db.query("""INSERT INTO poke_g3.breeding
( pokemon_id, gender_male, gender_female, egg_cycles)
VALUES((SELECT id FROM poke_g3.pokemon WHERE  pokedex_id = %s LIMIT 1),%s,%s,%s);""", 
(int(pokedex_id.iloc[i]),gender_male.iloc[i],gender_female.iloc[i],egg_cycles.iloc[i]))
    