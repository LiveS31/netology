-- Ok
create table if not exists compilacion(
	id_compilacion  INTEGER primary key, 
	names VARCHAR(60),
	year_output INTEGER
);

create table if not exists albums(
	id  INTEGER primary key,
	id_album INTEGER not null,
	album VARCHAR(60)not null,
	year_output INTEGER
);

create table if not exists executors (
	id  INTEGER primary key, 
	id_executors INTEGER not null, 
	executors VARCHAR(60)
);

create table if not exists title ( 
	id  INTEGER primary key, 
	genre VARCHAR(60) not null
);

create table if not exists song (
	id INTEGER primary key,
	id_song INTEGER not null references albums(id),
	song VARCHAR(60),
	track_time FLOAT
);

create table if not exists song_compilacion( 
	id_song INTEGER not null references song(id),
	id_compilacion INTEGER not null references compilacion(id_compilacion),
	constraint fpk primary key (id_song, id_compilacion)
);

create  table if not exists albub_executors (
	id_album INTEGER not null references albums(id),
	id_executors integer not null references executors(id),
	constraint fk primary key (id_album, id_executors)
);

create  table  if not exists title_executors(
	id_genres integer not null references title (id),
	id_executors integer not null references executors (id),
	constraint pk primary key (id_genres, id_executors)
);



