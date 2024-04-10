use poke_g3;

DROP PROCEDURE ObtenerInfoPokemon
DELIMITER //

CREATE PROCEDURE ObtenerInfoPokemon(IN pokedex_id_param VARCHAR(5))
BEGIN
    -- Variable para almacenar el ID del Pokémon
    DECLARE pokemon_id_var INT;

    -- Obtener el ID del Pokémon basado en el número de Pokédex proporcionado
    SELECT id INTO pokemon_id_var FROM pokemon WHERE pokedex_id = pokedex_id_param LIMIT 1;

    -- Verificar si se encontró un Pokémon con el número de Pokédex dado
    IF pokemon_id_var IS NOT NULL THEN
        -- Crear una tabla temporal para almacenar la información
        CREATE TEMPORARY TABLE temp_info_pokemon AS
        SELECT 
            p.id AS pokemon_id,
            p.pokedex_id,
            p.name,
            p.especie,
            p.height,
            p.weight,
            pbs.hp,
            pbs.attack,
            pbs.defense,
            pbs.special_attack,
            pbs.special_defense,
            pbs.speed,
            pbs.total,
            t.ev_yield,
            t.catch_rate,
            t.base_friendship,
            t.base_exp,
            t.growth_rate,
            b.gender_male As prob_male,
            b.gender_female As prob_feemale,
            b.egg_cycles,
            p2.name AS postevolucion,
            p3.name AS preevolucion
        FROM
            pokemon p
        LEFT JOIN
            pokemon_basic_stats pbs ON p.id = pbs.pokemon_id
        LEFT JOIN
            training t  ON p.id = t.pokemon_id 
        LEFT JOIN
            breeding b   ON p.id = b.pokemon_id 
        LEFT JOIN
            evolution_chart ec ON p.id = ec.pokemon_id 
        LEFT JOIN
            evolution_chart ec2 ON p.id = ec2.pokemon_evolution_id
        LEFT JOIN
            pokemon p2 ON p2.id = ec.pokemon_evolution_id 
        LEFT JOIN
            pokemon p3 ON p3.id = ec2.pokemon_id
        WHERE
            p.id = pokemon_id_var;

        -- Devolver la información almacenada en la tabla temporal
        SELECT DISTINCT * FROM temp_info_pokemon;
        
        -- Eliminar la tabla temporal
        DROP TEMPORARY TABLE IF EXISTS temp_info_pokemon;
       
       SELECT DISTINCT 
      		p1.name,
      		l.name As Language
      	FROM  pokemon_language p1
      	LEFT JOIN languages l on p1.language_id =l.id 
      WHERE pokemon_id =pokemon_id_var;
     
     SELECT DISTINCT 
      		eg.name 
      	FROM  breeding b 
      	LEFT JOIN egg_groups_breeding egb  on egb.breeding_id =b.id 
      	LEFT JOIN egg_groups eg  on egb.egg_group_id  =eg.id  
      WHERE b.pokemon_id =pokemon_id_var;
     
     SELECT DISTINCT 
      		gg.name as Juego,
      		pdgg.description 
      	FROM  pokemon_desc_gen_games pdgg  
      	LEFT JOIN gen_games gg   on pdgg.gen_game_id = gg.id 
      WHERE pdgg.pokemon_id =pokemon_id_var;
      
     SELECT DISTINCT 
      		m.*
      	FROM  pokemon_moves_bylevel pmb    
      	LEFT JOIN move m  on pmb.move_id  = m.id 
   
      WHERE pmb.pokemon_id =pokemon_id_var;
     
     SELECT DISTINCT 
     		gg.name as Juego,
      		l.location 
      	FROM  pokemon_location pl     
      	 JOIN location l  on pl.location_id  = l.id 
      	 JOIN gen_games gg on l.gen_games_id  = gg.id 
   
      WHERE pl.pokemon_id =pokemon_id_var;
    ELSE
        SELECT 'No se encontró ningún Pokémon con el número de Pokédex proporcionado';
    END IF;

END //

DELIMITER ;
CALL ObtenerInfoPokemon('0001');
CALL ObtenerInfoPokemon('0006');
CALL ObtenerInfoPokemon('0008');
CALL ObtenerInfoPokemon('0133');

CREATE PROCEDURE ObtenerLocationPokemon(IN pokedex_id_param VARCHAR(5))
BEGIN
    -- Variable para almacenar el ID del Pokémon
    DECLARE pokemon_id_var INT;

    -- Obtener el ID del Pokémon basado en el número de Pokédex proporcionado
    SELECT id INTO pokemon_id_var FROM pokemon WHERE pokedex_id = pokedex_id_param LIMIT 1;

    -- Verificar si se encontró un Pokémon con el número de Pokédex dado
    IF pokemon_id_var IS NOT NULL THEN
       
     SELECT DISTINCT 
     		gg.name as Juego,
     		gg.generation,
     		gg.region,
      		l.location 
      	FROM  pokemon_location pl     
      	 JOIN location l  on pl.location_id  = l.id 
      	 JOIN gen_games gg on l.gen_games_id  = gg.id 
   
      WHERE pl.pokemon_id =pokemon_id_var;
    ELSE
        SELECT 'No se encontró ningún Pokémon con el número de Pokédex proporcionado';
    END IF;

END

CALL ObtenerLocationPokemon('0001');
CALL ObtenerLocationPokemon('0006');
CALL ObtenerLocationPokemon('0008');
CALL ObtenerLocationPokemon('0133');


DELIMITER //
DROP PROCEDURE ObtenerCadenaEvolutiva
CREATE PROCEDURE ObtenerCadenaEvolutiva(IN pokedex_id_param VARCHAR(5))
BEGIN
    -- Variable para almacenar el ID del Pokémon
    DECLARE pokemon_id_var INT;
    
    -- Variable para almacenar el nombre del Pokémon
    DECLARE nombre_pokemon VARCHAR(100);
    
    SELECT id, name INTO pokemon_id_var, nombre_pokemon FROM pokemon WHERE pokedex_id = pokedex_id_param LIMIT 1;
    IF pokemon_id_var IS NOT NULL THEN
	
		WITH RECURSIVE cadena_evolutiva (
		  pokemon_id,
		  nameA,
		  nameE,
		  description,
		  pokemon_evolution_id,
		  nivel_evolucion
		) AS (
		  -- Seleccionamos el Pokémon inicial
		  SELECT
			e.pokemon_id,
			p.name,
			p2.name,
			e.description,
			e.pokemon_evolution_id,
			1 AS nivel_evolucion
		  FROM evolution_chart e 
		  JOIN pokemon p on p.id = e.pokemon_id
		  JOIN pokemon p2 on p2.id = e.pokemon_evolution_id 
		  WHERE e.pokemon_id = pokemon_id_var
	
		  UNION ALL
	
		  -- Seleccionamos los Pokémon siguientes
		  SELECT
			e.pokemon_evolution_id,
			p.name,
			p2.name,
			e.description,
			e.pokemon_evolution_id,
			ce.nivel_evolucion + 1
		  FROM cadena_evolutiva ce
	      LEFT JOIN evolution_chart e ON e.pokemon_id = ce.pokemon_evolution_id
	      LEFT JOIN pokemon p on p.id = e.pokemon_id
	      LEFT JOIN pokemon p2 on p2.id = e.pokemon_evolution_id 
		  WHERE ce.pokemon_evolution_id IS NOT NULL
		) SELECT DISTINCT  ce.nameA as pokemon, ce.nameE as evolucion, ce.description
		FROM cadena_evolutiva as ce
		WHERE ce.description is not null;
		
		WITH RECURSIVE cadena_involutiva (
		  pokemon_id,
		  nameA,
		  nameE,
		  description,
		  pokemon_evolution_id,
		  nivel_evolucion
		) AS (
		  -- Seleccionamos el Pokémon inicial
		  SELECT
			e.pokemon_id,
			p.name,
			p2.name,
			e.description,
			e.pokemon_evolution_id,
			1 AS nivel_evolucion
		  FROM evolution_chart e 
		  JOIN pokemon p on p.id = e.pokemon_id
		  JOIN pokemon p2 on p2.id = e.pokemon_evolution_id 
		  WHERE e.pokemon_evolution_id = pokemon_id_var 
	
		  UNION ALL
	
		  -- Seleccionamos los Pokémon anteriores
		  SELECT
			e.pokemon_id,
			p.name,
			p2.name,
			e.description,
			e.pokemon_id,
			ce.nivel_evolucion + 1
		  FROM cadena_involutiva ce
	      LEFT JOIN evolution_chart e ON e.pokemon_evolution_id = ce.pokemon_evolution_id
	      LEFT JOIN pokemon p on p.id = e.pokemon_id
	      LEFT JOIN pokemon p2 on p2.id = e.pokemon_evolution_id 
		  WHERE ce.pokemon_evolution_id IS NOT NULL
		)
		SELECT DISTINCT  ci.nameA as pokemon, ci.nameE as evolucion, ci.description
		FROM cadena_involutiva as ci
		WHERE ci.description is not null;
		        
    ELSE
        SELECT 'No se encontró ningún Pokémon con el número de Pokédex proporcionado';
    END IF;

END //

DELIMITER ;

CALL ObtenerCadenaEvolutiva('0001');
CALL ObtenerCadenaEvolutiva('0006');
CALL ObtenerCadenaEvolutiva('0008');
CALL ObtenerCadenaEvolutiva('0133');

DROP PROCEDURE ObtenerItemPokemon
CREATE PROCEDURE ObtenerItemPokemon(IN pokedex_id_param VARCHAR(5))
BEGIN
    -- Variable para almacenar el ID del Pokémon
    DECLARE pokemon_id_var INT;

    -- Obtener el ID del Pokémon basado en el número de Pokédex proporcionado
    SELECT id INTO pokemon_id_var FROM pokemon WHERE pokedex_id = pokedex_id_param LIMIT 1;

    -- Verificar si se encontró un Pokémon con el número de Pokédex dado
    IF pokemon_id_var IS NOT NULL THEN
       
     SELECT DISTINCT 
     		i.name,
     		ec.description 
      	FROM  evolution_chart ec      
      	LEFT JOIN item i   on ec.item_id  = i.id 
      WHERE ec.pokemon_id  =pokemon_id_var or ec.pokemon_evolution_id = pokemon_id_var;
    ELSE
        SELECT 'No se encontró ningún Pokémon con el número de Pokédex proporcionado';
    END IF;

END

CALL ObtenerItemPokemon('0199');
CALL ObtenerItemPokemon('0006');
CALL ObtenerItemPokemon('0008');
CALL ObtenerItemPokemon('0133');