import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/evoluciones/pokemoneses.csv')

# Evolving_from,Evolving_to,level,item,description,type
Evolving_from = data['Evolving_from']
Evolving_to = data['Evolving_to']
item = data['item']
description = data['description']
for i in range(len(Evolving_from)):
        objt="nulo"
        if str(item.iloc[i])!="nan":
            objt=item.iloc[i]
        db.query_con_retorno("""INSERT INTO poke_g3.evolution_chart
    (pokemon_id, pokemon_evolution_id, level, item_id, description, type_evolution)
    VALUES((SELECT id FROM poke_g3.pokemon WHERE name = %s ),(SELECT id FROM poke_g3.pokemon WHERE name = %s ),
        %s,(SELECT id FROM poke_g3.item WHERE name = %s),%s,(SELECT id FROM poke_g3.type_evolution WHERE name = %s));""",
    (Evolving_from.iloc[i],Evolving_to.iloc[i],0,objt,description.iloc[i],"other"))
              