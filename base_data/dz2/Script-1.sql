-- Ok
-- Создание таблиц
-- сборник
create table if not exists compilacion(
	id_compilacion  SERIAL primary key,
	names  text not null,
	year_output INTEGER
);
-- альбом
create table if not exists albums(
	id  SERIAL primary key,
	album TEXT not null,
	year_output INTEGER
);
-- исполнитель
create table if not exists executors (
	id  SERIAL primary key,
	name text not null
);
-- жанр
create table if not exists genre(
	id  SERIAL primary key,
	genre VARCHAR(50) not null
);
-- песня
create table if not exists song(
	id SERIAL primary key,
	album_id INTEGER not null references albums(id),
	song TEXT,
	track_time FLOAT
);
-- промежуточные таблицы
create table if not exists song_compilacion(
	id_compilacion INTEGER not null references compilacion(id_compilacion),
	id_song INTEGER not null references song(id),
	constraint fpk primary key (id_song, id_compilacion)
);

create  table if not exists album_executors (
	id_album SERIAL not null references albums(id),
	id_executors SERIAL not null references executors(id),
	constraint fk primary key (id_album, id_executors)
);

create  table  if not exists genge_executors(
	id_genres integer not null references genre(id),
	id_executors integer not null references executors(id),
	constraint pk primary key (id_genres, id_executors)
);
