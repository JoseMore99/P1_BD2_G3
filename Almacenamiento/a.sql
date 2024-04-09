create table move_categories(
	id integer AUTO_INCREMENT primary key, 
	name varchar(50)
);

create table types(
	id integer AUTO_INCREMENT primary key, 
	name varchar(50)
);

create table types_vs_types(
	id integer AUTO_INCREMENT primary key,
	type1 integer,
	type2 integer,
	is_weak tinyint,
	foreign key (type1) references types(id),
	foreign key (type2) references types(id)
);

create table nature(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);

create table ability(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);

create table item_category (
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);

create table item(
	id integer AUTO_INCREMENT primary key,
	name varchar(30),
	effect varchar(200),
	category integer not null,
	foreign key (category) references item_category(id)
);

create table gen_games(
	id integer AUTO_INCREMENT primary key,
	generation varchar(25),
	name varchar(50),
	region varchar(50)
);

create table item_desc_gen_games(
	id integer AUTO_INCREMENT primary key,
	gen_game_id integer,
	item_id integer,
	description varchar(100),
	foreign key (gen_game_id) references gen_games(id),
	foreign key (item_id) references item(id)
);

create table ability_desc_gen_games(
	id integer AUTO_INCREMENT primary key,
	gen_game_id integer,
	ability_id integer,
	description varchar(100),
	foreign key (gen_game_id) references gen_games(id),
	foreign key(ability_id) references ability(id)
);

create table egg_groups(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);

create table type_evolution(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);

create table languages(
	id integer AUTO_INCREMENT primary key,
	name varchar(50)
);

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

create table location (
    id integer auto_increment primary key ,
    gen_games_id integer   ,
    location varchar(100),
    foreign key (gen_games_id) references gen_games(id)
);

create table move(
    id integer auto_increment primary key ,
    name varchar(100),
    type integer,
    move_category integer,
    power integer,
    accuracy integer,
    effect varchar(100),
    foreign key (type) references types(id),
    foreign key (move_category) references move_categories(id)
);

create table pokemon_moves(
    id integer auto_increment primary key ,
    pokemon_id integer,
    move_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key  (move_id) references  move(id)
);

create table breeding(
    id integer auto_increment primary key ,
    pokemon_id integer,
    gender_male numeric,
    gender_female numeric,
    egg_cycles integer,
    foreign key (pokemon_id) references pokemon(id)
);

create table training(
    id integer auto_increment primary key ,
    pokemon_id integer,
    ev_yield varchar(30),
    catch_rate numeric,
    base_friendship numeric,
    base_exp numeric,
    growth_rate varchar(30),
    foreign key (pokemon_id) references pokemon(id)
);

create table pokemon_type(
    id integer auto_increment primary key ,
    pokemon_id integer,
    type_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key (type_id) references types(id)
);

create table egg_groups_breeding(
    id integer auto_increment primary key ,
    breeding_id integer,
    egg_group_id integer,
    foreign key (breeding_id) references breeding(id),
    foreign key (egg_group_id) references egg_groups(id)
);

create table move_des_gen_games(
    id integer auto_increment primary key ,
    gen_game_id integer,
    move_id integer,
    description varchar(100),
    foreign key (gen_game_id) references gen_games(id),
    foreign key (move_id) references move(id)
);

create table pokemon_location(
    id integer auto_increment primary key ,
    pokemon_id integer,
    location_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key (location_id) references location(id)
);

create table pokemon_hability(
    id integer auto_increment primary key ,
    pokemon_id integer,
    ability_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key (ability_id) references ability(id)
);

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

create table special_forms(
    id integer auto_increment primary key ,
    pokemon_id integer,
    description varchar(200),
    item_id integer,
    move_id integer,
    foreign key (pokemon_id) references pokemon(id),
    foreign key (item_id) references  item(id),
    foreign key  (move_id) references  move(id)
);