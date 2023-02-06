create table if not exists title ( 
id INTEGER primary key, 
genre TEXT
);

create table if not exists executors (
id INTEGER primary key ,
id_executors INTEGER references title(id),
executors VARCHAR(60)
);

create table if not exists album (
	id INTEGER primary key,
	id_album INTEGER references executors(id),
	album TEXT,
	year_output INTEGER
	);

create table if not exists song (
id INTEGER primary key,
id_song INTEGER references album(id),
song VARCHAR(60),
track_time INTEGER
);

create table if not exists compilacion (
id SERIAL primary key,
id_album INTEGER not null references album(id),
id_song INTEGER not null references song(id),
id_genre INTEGER not null references title(id)
);