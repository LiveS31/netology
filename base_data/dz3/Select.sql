-- Ok
-- выботка по году
SELECT album, year_output FROM albums
WHERE year_output = 2018;

-- Максимально время 
SELECT song , track_time FROM song
ORDER BY track_time desc
limit 1;

-- не менее 3,5 минуты;
SELECT song  FROM song
WHERE track_time >= (3.5*60);


-- Сборники 2018 - 2020 
SELECT names, year_output FROM compilation 
WHERE year_output >= 2003 and year_output <= 2018 ;

--исполнители, чье имя состоит из 1 слова
SELECT name from executors 
WHERE name not like '% %';

-- название треков, которые содержат слово "мой"/"my"
SELECT song  from song
WHERE song like '%my%';

SELECT song  from song
WHERE song like '%мой%';

