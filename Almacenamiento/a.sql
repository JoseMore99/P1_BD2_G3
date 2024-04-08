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