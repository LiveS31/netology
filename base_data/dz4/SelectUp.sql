 
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
-- год был выведен для наглядности
select  e."name", a.year_output  from albums a
join album_executors ae on a.id = ae.id_album
join executors e on ae.id_album = e.id
where a.year_output != 2020;

-- 5.названия сборников, в которых присутствует конкретный исполнитель 
--(выберите сами);
-- названия сборников,
--в которых присутствует конкретный исполнитель (выберите сами);
select   c.names, e."name"  from compilation c
join song_compilation sc on c.id_compilation = sc.id_compilation
join song s on sc.id_song  = s.id
join album_executors ae on s.id = ae.id_executors
join executors e on ae.id_album = e.id
where e."name" = 'Antonio Vivaldi';

-- 6.название альбомов, в которых присутствуют исполнители более 1 жанра;
SELECT a.album   FROM albums a
JOIN album_executors ae on a.id = ae.id_album
JOIN executors e ON ae.id_executors  = e.id
JOIN genre_executors ge ON e.id = ge.id_executors
JOIN genre g ON ge.id_genres  = g.id
GROUP BY a.album, g.genre
HAVING COUNT(g.id) > 1;

-- 7.наименование треков, которые не входят в сборники;
SELECT  s.id ,s.song  FROM song s
left join song_compilation sc on sc.id_song  = s.id
where  sc.id_song is  null;

--8.исполнителя(-ей), написавшего самый короткий по продолжительности трек
-- (теоретически таких треков может быть несколько);
-- Выведено для удобства
select  e."name", s."song",s.track_time   from song s
join albums a on s.album_id  = a.id
join album_executors ae on a.id = ae.id_album
join executors e on ae.id_executors  = e.id
WHERE s.track_time  < (SELECT MAX(s.track_time) FROM song s)
ORDER BY s.track_time
limit 1;

-- 9.название альбомов, содержащих наименьшее количество треков.
-- в альбом была добавлена +1 композиция ( так как в альбомах было по 2 трека)
-- выведено для удобства
SELECT  a.album , COUNT(*) FROM song s
join albums a on s.album_id = a.id
GROUP BY s.album_id , a.id
HAVING COUNT(*) != (select sum(album_id));