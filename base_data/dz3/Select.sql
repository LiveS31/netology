-- выботка по году
SELECT album, year_output FROM albums
WHERE year_output = 2018;

-- Максимально время 
SELECT song , track_time FROM song
ORDER BY track_time desc
limit 1;

-- Менее 3,5 минут
SELECT song , track_time FROM song
WHERE track_time < 3.5;

-- Сборники 2018 - 2020 ?????
-- Непонял как сделать, и помощь в чате молчит.....

SELECT  year_output
FROM albub_executors 
WHERE year_output >= 2003 and year_output <= 2018 ;



--исполнители, чье имя состоит из 1 слова
SELECT executors from executors 
WHERE executors not like '% %';

-- название треков, которые содержат слово "мой"/"my"
select song  from song
WHERE song like '%my%';

select song  from song
WHERE song like '%мой%';

