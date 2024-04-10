
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
		  name,
		  description,
		  pokemon_evolution_id,
		  nivel_evolucion
		) AS (
		  -- Seleccionamos el Pokémon inicial
		  SELECT
		    p.id,
		    p.name,
		    e.description,
		    e.pokemon_evolution_id,
		    1 AS nivel_evolucion
		  FROM pokemon p
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id 
		  WHERE p.id = pokemon_id_var
		
		  UNION ALL
		
		  -- Seleccionamos los Pokémon siguientes
		  SELECT
		    e.pokemon_evolution_id,
		    p.name,
		    e2.description,
		    e2.pokemon_evolution_id,
		    nivel_evolucion + 1
		  FROM cadena_evolutiva ce
		  LEFT JOIN pokemon p ON ce.pokemon_evolution_id = p.id 
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id 
		  LEFT JOIN evolution_chart e2 ON e.pokemon_evolution_id = e2.pokemon_id
		  WHERE ce.pokemon_evolution_id IS NOT NULL
		  
		  
		)
		SELECT name, description
		FROM cadena_evolutiva
		WHERE nivel_evolucion 
		ORDER BY nivel_evolucion ASC;
	
	WITH RECURSIVE cadena_inevolutiva (
		  pokemon_id,
		  name,
		  description,
		  pokemon_evolution_id,
		  nivel_evolucion
		) AS (
		  -- Seleccionamos el Pokémon inicial
		  SELECT
		    p.id,
		    p.name,
		    e.description,
		    e.pokemon_evolution_id,
		    1 AS nivel_evolucion
		  FROM pokemon p
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id 
		  WHERE p.id = pokemon_id_var
		
		  UNION ALL
		
		  -- Seleccionamos los Pokémon anteriores
		  SELECT
		    e.pokemon_id,
		    p.name,
		    e2.description,
		    e2.pokemon_id,
		    nivel_evolucion - 1
		  FROM cadena_inevolutiva ce
		  LEFT JOIN pokemon p ON ce.pokemon_id = p.id 
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_evolution_id 
		  LEFT JOIN evolution_chart e2 ON e.pokemon_id = e2.pokemon_id
		  WHERE ce.pokemon_id IS NOT NULL
		)
		SELECT name, description
		FROM cadena_inevolutiva
		WHERE nivel_evolucion 
		ORDER BY nivel_evolucion ASC;

	        
    ELSE
        SELECT 'No se encontró ningún Pokémon con el número de Pokédex proporcionado';
    END IF;

END //

DELIMITER ;

CALL ObtenerCadenaEvolutiva('0026')




WITH RECURSIVE cadena_evolutiva (
  pokemon_id,
  name,
  pokemon_evolution_id,
  nivel_evolucion
) AS (
  -- Seleccionamos el Pokémon inicial
  SELECT
    p.id,
    p.name,
    e.pokemon_evolution_id,
    1 AS nivel_evolucion
  FROM pokemon p
  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id
  WHERE p.id = @pokemon_id

  UNION ALL

  -- Seleccionamos los Pokémon siguientes
  SELECT
    e.pokemon_evolution_id AS pokemon_id,
    p.name as name,
    e2.pokemon_evolution_id as pokemon_evolution_id,
    nivel_evolucion + 1 as nivel_evolucion
  FROM cadena_evolutiva ce
  LEFT JOIN pokemon p ON ce.pokemon_evolution_id = p.id
  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id
  LEFT JOIN evolution_chart e2 ON e.pokemon_evolution_id = e2.pokemon_id
  WHERE ce.pokemon_evolution_id IS NOT NULL
)
SELECT *
FROM cadena_evolutiva
WHERE nivel_evolucion
ORDER BY nivel_evolucion ASC;


---------------------------------------------------------
set @pokemon_id = 226;
WITH  RECURSIVE cadena_evolutiva (
		  pokemon_id,
		  name,
		  description,
		  pokemon_evolution_id,
		  nivel_evolucion
		) AS (
		  -- Seleccionamos el Pokémon inicial
		  SELECT
		    p.id,
		    p.name,
		    e.description,
		    e.pokemon_evolution_id,
		    1 AS nivel_evolucion
		  FROM pokemon p
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id 
		  WHERE p.id = @pokemon_id
		
		  UNION ALL
		
		  -- Seleccionamos los Pokémon siguientes
		  SELECT
		    ce.pokemon_evolution_id,
		    p2.name,
		    e.description,
		    e2.pokemon_evolution_id,
		    nivel_evolucion + 1
		  FROM cadena_evolutiva ce
		  LEFT JOIN pokemon p ON ce.pokemon_evolution_id = p.id 
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id 
		  LEFT JOIN evolution_chart e2 ON e.pokemon_evolution_id = e2.pokemon_id
		  LEFT JOIN pokemon p2 ON e2.pokemon_id = p2.id
		  WHERE ce.pokemon_evolution_id IS NOT NULL
		  
		  
		), cadena_inevolutiva (
		  pokemon_id,
		  name,
		  description,
		  pokemon_evolution_id,
		  nivel_evolucion
		) AS (
		  -- Seleccionamos el Pokémon inicial
		  SELECT
		    p.id,
		    p.name,
		    e.description,
		    e.pokemon_evolution_id,
		    1 AS nivel_evolucion
		  FROM pokemon p
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id 
		  WHERE p.id = @pokemon_id
		
		  UNION ALL
		
		  -- Seleccionamos los Pokémon anteriores
		  SELECT
		    e.pokemon_id,
		    p.name,
		    e2.description,
		    e2.pokemon_id,
		    nivel_evolucion - 1
		  FROM cadena_inevolutiva ce
		  LEFT JOIN pokemon p ON ce.pokemon_id = p.id 
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_evolution_id 
		  LEFT JOIN evolution_chart e2 ON e.pokemon_id = e2.pokemon_id
		  WHERE ce.pokemon_id IS NOT NULL
		)
		SELECT DISTINCT ce.*
		FROM cadena_evolutiva as ce
		
SELECT * FROM evolution_chart ec WHERE ec.pokemon_evolution_id = 35

WITH  RECURSIVE cadena_evolutiva (
		  pokemon_id,
		  name,
		  nameS,
		  description,
		  pokemon_evolution_id,
		  nivel_evolucion
		) AS (
		  -- Seleccionamos el Pokémon inicial
		  SELECT
		    @pokemon_id,
		    p.name,
		    p2.name,
		    e.description,
		    e.pokemon_evolution_id,
		    1 AS nivel_evolucion
		  FROM evolution_chart e 
		  JOIN pokemon p on p.id = e.pokemon_evolution_id
		  JOIN pokemon p2 on p2.id = e.pokemon_id 
		  WHERE e.pokemon_id = pokemon_id 
		
		  UNION ALL
		
		  -- Seleccionamos los Pokémon siguientes
		  SELECT
		    e.pokemon_evolution_id,
		    p.name,
		    ce.name,
		    e2.description,
		    e2.pokemon_evolution_id,
		    nivel_evolucion + 1
		  FROM cadena_evolutiva ce
		  LEFT JOIN pokemon p ON ce.pokemon_evolution_id = p.id 
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id 
		  LEFT JOIN evolution_chart e2 ON e.pokemon_evolution_id = e2.pokemon_id
		  WHERE ce.pokemon_evolution_id IS NOT NULL
		  
		  
		), cadena_inevolutiva (
		  pokemon_id,
		  name,
		  description,
		  pokemon_evolution_id,
		  nivel_evolucion
		) AS (
		  -- Seleccionamos el Pokémon inicial
		  SELECT
		    p.id,
		    p.name,
		    e.description,
		    e.pokemon_evolution_id,
		    1 AS nivel_evolucion
		  FROM pokemon p
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_id 
		  WHERE p.id = @pokemon_id
		
		  UNION ALL
		
		  -- Seleccionamos los Pokémon anteriores
		  SELECT
		    e.pokemon_id,
		    p.name,
		    e2.description,
		    e2.pokemon_id,
		    nivel_evolucion - 1
		  FROM cadena_inevolutiva ce
		  LEFT JOIN pokemon p ON ce.pokemon_id = p.id 
		  LEFT JOIN evolution_chart e ON p.id = e.pokemon_evolution_id 
		  LEFT JOIN evolution_chart e2 ON e.pokemon_id = e2.pokemon_id
		  WHERE ce.pokemon_id IS NOT NULL
		)
		SELECT DISTINCT ce.name as evolucion, ce.nameS as preevolucion, ce.description
		FROM cadena_evolutiva as ce
		

