create database poke_g3;

use poke_g3;
--LISTO
create table move_categories(
	id integer AUTO_INCREMENT primary key, 
	name varchar(50)
);
SELECT * FROM move_categories
--LISTO
create table types(
	id integer AUTO_INCREMENT primary key, 
	name varchar(50)
);
SELECT * from types 
--PENDIENTE
create table types_vs_types(
	id integer AUTO_INCREMENT primary key,
	type1 integer,
	type2 integer,
	is_weak tinyint,
	foreign key (type1) references types(id),
	foreign key (type2) references types(id)
);
--PENDIENTE
create table nature(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);
SELECT * FROM nature n 

--LISTO
drop table ability
create table ability(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);

SELECT * FROM ability
--LISTO
create table item_category (
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);
SELECT * FROM item_category

--LISTO
drop table item
create table item(
	id integer AUTO_INCREMENT primary key,
	name varchar(30),
	effect varchar(200),
	category integer not null,
	foreign key (category) references item_category(id)
);
	SELECT *  FROM item i 
--LISTO
drop table gen_games
create table gen_games(
	id integer AUTO_INCREMENT primary key,
	generation varchar(25),
	name varchar(50),
	region varchar(50)
);
SELECT  * FROM gen_games
--LISTO
drop table item_desc_gen_games
create table item_desc_gen_games(
	id integer AUTO_INCREMENT primary key,
	gen_game_id integer,
	item_id integer,
	description varchar(250),
	foreign key (gen_game_id) references gen_games(id),
	foreign key (item_id) references item(id)
);
SELECT *  FROM item_desc_gen_games 

--LISTO
drop table ability_desc_gen_games
create table ability_desc_gen_games(
	id integer AUTO_INCREMENT primary key,
	gen_game_id integer,
	ability_id integer,
	description varchar(250),
	foreign key (gen_game_id) references gen_games(id),
	foreign key(ability_id) references ability(id)
);
SELECT *  FROM ability_desc_gen_games

--LISTO
create table egg_groups(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);
SELECT *  FROM egg_groups

--LISTO
create table type_evolution(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);
SELECT *  FROM type_evolution

--LISTO
create table languages(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);
SELECT *  FROM languages

--LISTO
drop table pokemon
create table pokemon(
	id integer AUTO_INCREMENT primary key, 
	pokedex_id varchar(5),
	name varchar(100),
	especie varchar(100),
	height varchar(30),
	weight varchar(30),
	id_nature integer,
	foreign key (id_nature) references nature(id)
);
SELECT COUNT(*)  FROM pokemon 
SELECT *  FROM pokemon 

--LISTO
create table location (
    id integer auto_increment primary key ,
    gen_games_id integer   ,
    location varchar(100),
    foreign key (gen_games_id) references gen_games(id)
);
SELECT * FROM location
--LISTO
drop table move
create table move(
    id integer auto_increment primary key ,
    name varchar(100),
    type integer,
    move_category integer,
    power integer,
    accuracy integer,
    effect varchar(200),
    foreign key (type) references types(id),
    foreign key (move_category) references move_categories(id)
);
SELECT * FROM move
--LISTO
drop table pokemon_moves_bylevel
create table pokemon_moves_bylevel(
    id integer auto_increment primary key ,
    pokemon_id integer,
    move_id integer,
    level integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key  (move_id) references  move(id)
);
SELECT * FROM pokemon_moves_bylevel
--LISTO
drop table breeding
create table breeding(
    id integer auto_increment primary key ,
    pokemon_id integer,
    gender_male varchar(20),
    gender_female varchar(20),
    egg_cycles varchar(100),
    foreign key (pokemon_id) references pokemon(id)
);
SELECT * FROM breeding
SELECT * FROM pokemon

--LISTO
drop table training 
create table training(
    id integer auto_increment primary key ,
    pokemon_id integer,
    ev_yield varchar(30),
    catch_rate varchar(30),
    base_friendship varchar(30),
    base_exp numeric,
    growth_rate varchar(30),
    foreign key (pokemon_id) references pokemon(id)
);
SELECT * FROM training

--LISTO
create table pokemon_type(
    id integer auto_increment primary key ,
    pokemon_id integer,
    type_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key (type_id) references types(id)
);
SELECT * FROM pokemon_type

--LISTO
create table egg_groups_breeding(
    id integer auto_increment primary key ,
    breeding_id integer,
    egg_group_id integer,
    foreign key (breeding_id) references breeding(id),
    foreign key (egg_group_id) references egg_groups(id)
);
SELECT * FROM egg_groups_breeding

--LISTO
create table move_des_gen_games(
    id integer auto_increment primary key ,
    gen_game_id integer,
    move_id integer,
    description varchar(250),
    foreign key (gen_game_id) references gen_games(id),
    foreign key (move_id) references move(id)
);
SELECT * FROM move_des_gen_games

--LISTO
drop table pokemon_location
create table pokemon_location(
    id integer auto_increment primary key ,
    pokemon_id integer,
    location_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key (location_id) references location(id)
);
SELECT * FROM pokemon_location

--LISTO
drop table pokemon_ability 
create table pokemon_ability(
    id integer auto_increment primary key ,
    pokemon_id integer,
    ability_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key (ability_id) references ability(id)
);
SELECT * FROM ability
--LISTO
create table pokemon_basic_stats(
    id integer auto_increment primary key ,
    pokemon_id integer,
    hp numeric,
    attack numeric,
    defense numeric,
    special_attack numeric,
    special_defense numeric,
    speed numeric,
    total numeric,
    foreign key (pokemon_id) references  pokemon(id)
);
SELECT * FROM pokemon_basic_stats
--LISTO
drop table evolution_chart
create table evolution_chart(
    id integer auto_increment primary key ,
    pokemon_id integer,
    pokemon_evolution_id integer,
    level integer,
    item_id integer,
    description varchar(200),
    type_evolution integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key  (pokemon_evolution_id) references pokemon(id),
    foreign key (item_id) references item(id),
    foreign key  (type_evolution) references  type_evolution(id)
);

--LISTO
drop table pokemon_language 
create table pokemon_language(
	id integer auto_increment primary key ,
    pokemon_id integer,
    language_id integer,
    name varchar(100),
    foreign key  (pokemon_id) references pokemon(id),
    foreign key  (language_id) references languages(id)
);
--LISTO
DROP table pokemon_desc_gen_games 
create table pokemon_desc_gen_games(
	id integer AUTO_INCREMENT primary key,
	gen_game_id integer,
	pokemon_id integer,
	description varchar(300),
	foreign key (gen_game_id) references gen_games(id),
	foreign key(pokemon_id) references pokemon(id)
);
SELECT * FROM pokemon_desc_gen_games pdgg 

drop table pokemon_moves_byegg
create table pokemon_moves_byegg(
    id integer auto_increment primary key ,
    pokemon_id integer,
    move_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key  (move_id) references  move(id)
);
SELECT * FROM pokemon_moves_byegg

drop table pokemon_moves_byTM
create table pokemon_moves_byTM(
    id integer auto_increment primary key ,
    pokemon_id integer,
    move_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key  (move_id) references  move(id)
);
SELECT * FROM pokemon_moves_byTM