import db
import pandas as pd
import ast


# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/evoluciones/evos3.csv')
data2 = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/evoluciones/evos2.csv')

# Evolving_from,Evolving_to,level,item,description,type
Evolving_from = data['Evolving_from']
Evolving_to = data['Evolving_to']
level = data['level']
item = data2['item']
description = data['description']
type = data['type']
for i in range(len(Evolving_from)):
        objt="nulo"
        if str(item.iloc[i])!="nan":
            objt=item.iloc[i]
        if str(description.iloc[i])=="nan":
            print((Evolving_from.iloc[i],Evolving_to.iloc[i],level.iloc[i],objt," ",type.iloc[i]))
            db.query_con_retorno("""INSERT INTO poke_g3.evolution_chart
    (pokemon_id, pokemon_evolution_id, level, item_id, description, type_evolution)
    VALUES((SELECT id FROM poke_g3.pokemon WHERE name = %s ),(SELECT id FROM poke_g3.pokemon WHERE name = %s ),
        %s,(SELECT id FROM poke_g3.item WHERE name = %s),%s,(SELECT id FROM poke_g3.type_evolution WHERE name = %s));""",
    (Evolving_from.iloc[i],Evolving_to.iloc[i],level.iloc[i],objt," ",type.iloc[i]))
        else:
            db.query_con_retorno("""INSERT INTO poke_g3.evolution_chart
    (pokemon_id, pokemon_evolution_id, level, item_id, description, type_evolution)
    VALUES((SELECT id FROM poke_g3.pokemon WHERE name = %s ),(SELECT id FROM poke_g3.pokemon WHERE name = %s ),
        %s,(SELECT id FROM poke_g3.item WHERE name = %s),%s,(SELECT id FROM poke_g3.type_evolution WHERE name = %s));""",
    (Evolving_from.iloc[i],Evolving_to.iloc[i],level.iloc[i],objt,description.iloc[i],type.iloc[i]))
              