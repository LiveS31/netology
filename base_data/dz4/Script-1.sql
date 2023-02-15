-- Ok
-- Создание таблиц
-- Cборник
create table if not exists compilation(
	id_compilation  SERIAL primary key,
	names  text ,
	year_output INTEGER not null
);

-- альбом
create table if not exists albums(
	id  SERIAL primary key,
	album TEXT not null,
	year_output INTEGER
);

-- исполнитель
create table if not exists executors (
	id  SERIAL primary key not null,
	name TEXT
);

-- жанр
create table if not exists genre(
	id  SERIAL primary key,
	genre VARCHAR(50)
);

-- песня
create table if not exists song(
	id SERIAL primary key,
	album_id INTEGER not null references albums(id),
	song TEXT,
	track_time INTEGER not null
);

-- промежуточные таблицы
-- добавлена колонка id SERIAL not null,
create table if not exists song_compilation(
	id_compilation INTEGER not null references compilation(id_compilation),
	id_song INTEGER not null references song(id),
	constraint fpk primary key (id_compilation, id_song)
);

create  table if not exists album_executors (
	id_album SERIAL not null references albums(id),
	id_executors SERIAL not null references executors(id),
	constraint fk primary key (id_album, id_executors)
);
-- +дополнено
create  table  if not exists genre_executors(
	id_genres integer not null references genre(id),
	id_executors integer not null references executors(id),
	constraint ptk primary key (id_genres, id_executors)
);
