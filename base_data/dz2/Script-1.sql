-- Ok
-- Создание таблиц
create table if not exists compilacion(
	id_compilacion  INTEGER primary key,
	names TEXT,
	year_output INTEGER
);

create table if not exists albums(
	id  INTEGER primary key,
	album TEXT not null,
	year_output INTEGER
);

create table if not exists executors (
	id  INTEGER primary key,
	executors VARCHAR(60)
);

create table if not exists genre(
	id  INTEGER primary key,
	genre VARCHAR(50) not null
);

create table if not exists song(
	id INTEGER primary key,
	album_id INTEGER not null references albums(id),
	album_id2 INTEGER references albums(id),
	song TEXT,
	track_time FLOAT
);

create table if not exists song_compilacion(
	id_song INTEGER not null references song(id),
	id_compilacion INTEGER not null references compilacion(id_compilacion),
	constraint fpk primary key (id_song, id_compilacion)
);

create  table if not exists album_executors (
	id_album INTEGER not null references albums(id),
	id_executors integer not null references executors(id),
	constraint fk primary key (id_album, id_executors)
);

create  table  if not exists genge_executors(
	id_genres integer not null references genre(id),
	id_executors integer not null references executors(id),
	constraint pk primary key (id_genres, id_executors)
);
