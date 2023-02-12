 
-- 1. количество исполнителей в каждом жанре;
select genre.genre, count(genre_executors.id_executors) from genre
join genre_executors on genre.id = genre_executors.id_genres
group by genre.genre

-- 2.количество треков, вошедших в альбомы 2019-2020 годов;
select count(song.id) from song
join albums a  on song.album_id = a.id
where  year_output >= 2019 and year_output <= 2022 ;

-- 3.средняя продолжительность треков по каждому альбому;
select a.album, avg(s.track_time) from albums a
join song s on a.id  = s.album_id
group by a.id ;

-- 4.все исполнители, которые не выпустили альбомы в 2020 году;

-- 5.названия сборников, в которых присутствует конкретный исполнитель 
--(выберите сами);

-- 6.название альбомов, в которых присутствуют исполнители более 1 жанра;

-- 7.наименование треков, которые не входят в сборники;

-- 8.исполнителя(-ей), написавшего самый короткий по продолжительности трек 
-- (теоретически таких треков может быть несколько);

-- 9.название альбомов, содержащих наименьшее количество треков.
