-- заполнение жанр
INSERT INTO title(id, genre)
VALUES(1, 'ROCK');

INSERT INTO title(id, genre)
VALUES(2, 'POP');

INSERT INTO title(id, genre)
VALUES(3, 'Jazz');

INSERT INTO title(id, genre)
VALUES(4, 'Classic');

INSERT INTO title(id, genre)
VALUES(5, 'RAP');

-- заполнение испотнители
INSERT INTO executors(id,id_executors, executors)
VALUES(1, 1, 'Queen');

INSERT INTO executors(id, id_executors, executors)
VALUES(2, 1, 'Linkin Park');

INSERT INTO executors(id, id_executors, executors)
VALUES(3, 1, 'Red Hot Chili Peppers');

INSERT INTO executors(id, id_executors, executors)
VALUES(4, 2, 'Ariana Grande');

INSERT INTO executors(id, id_executors, executors)
VALUES(5, 2, 'Lady Gaga');

INSERT INTO executors(id, id_executors, executors)
VALUES(6, 3, 'Louis Armstrong');

INSERT INTO executors(id,id_executors, executors)
VALUES(7, 3, 'Duke Ellington');

INSERT INTO executors(id,id_executors, executors)
VALUES(8, 4, 'Johann Sebastian Bach');

INSERT INTO executors(id,id_executors, executors)
VALUES(9, 4, 'Antonio Vivaldi');

INSERT INTO executors(id, id_executors, executors)
VALUES(10, 5, 'Centr');

INSERT INTO executors(id, id_executors, executors)
VALUES(11, 5, 'Slim');

-- заполнение альбомов
INSERT INTO album(id, id_album, album, year_output)
VALUES(1, 1, 'Sheer Heart Attack', '1974');

INSERT INTO album(id, id_album, album, year_output)
VALUES(2, 1, 'A Night at the Opera', '1975');

INSERT INTO album(id, id_album, album, year_output)
VALUES(3, 2, 'Hybrid Theory', '2000');

INSERT INTO album(id, id_album, album, year_output)
VALUES(4, 2, 'Meteora', '2003');

INSERT INTO album(id, id_album, album, year_output)
VALUES(5, 3, 'Californication', '1999');

INSERT INTO album(id, id_album, album, year_output)
VALUES(6, 3, 'Stadium Arcadium', '2006');

INSERT INTO album(id, id_album, album, year_output)
VALUES(7, 4, 'Sweetener', '2018');

INSERT INTO album(id, id_album, album, year_output)
VALUES(8, 4, 'My Everything', '2014');

INSERT INTO album(id, id_album, album, year_output)
VALUES(9, 5, 'MChromatica', '2020');

INSERT INTO album(id, id_album, album, year_output)
VALUES(10, 5, 'Artpop', '2013');

INSERT INTO album(id, id_album, album, year_output)
VALUES(11, 6, 'Ella and Louis', '1956');

INSERT INTO album(id, id_album, album, year_output)
VALUES(12, 6, 'Satchmo', '1958');

INSERT INTO album(id, id_album, album, year_output)
VALUES(13, 7, 'Piano Reflections', '1953');

INSERT INTO album(id, id_album, album, year_output)
VALUES(14, 7, 'Duke Ellington & John Coltrane', '1963');

INSERT INTO album(id, id_album, album, year_output)
VALUES(15, 8, 'Violin Concertos', '1986');

INSERT INTO album(id, id_album, album, year_output)
VALUES(16, 8, 'The Goldberg Variations', '2007');

INSERT INTO album(id, id_album, album, year_output)
VALUES(17, 9, 'The Four Seasons', '1970');

INSERT INTO album(id, id_album, album, year_output)
VALUES(18, 9, 'Vivaldi', '1967');


INSERT INTO album(id, id_album, album, year_output)
VALUES(19, 10, 'Легенды про…Centr', '2011');

INSERT INTO album(id, id_album, album, year_output)
VALUES(20, 10, 'Качели', '2007');


INSERT INTO album(id, id_album, album, year_output)
VALUES(21, 11, 'GUSLI', '2017');

INSERT INTO album(id, id_album, album, year_output)
VALUES(22, 11, 'Вид на жизнь', '2022');

-- Добовка треков
INSERT INTO song(id, id_song, song, track_time)
VALUES(1, 1, 'Dear Friends', '1:09');

INSERT INTO song(id, id_song, song, track_time)
VALUES(2, 1, 'Brighton Rock', '5:11');

INSERT INTO song(id, id_song, song, track_time)
VALUES(3, 2, 'Sweet Lady', '5:11');

INSERT INTO song(id, id_song, song, track_time)
VALUES(4, 2, 'Death On Two Legs (Dedicated To...)', '3:44');

INSERT INTO song(id, id_song, song, track_time)
VALUES(5, 3, 'Enth E Nd', '4:00');

INSERT INTO song(id, id_song, song, track_time)
VALUES(6, 3, 'P5hng Me A*wy', '4:38');

INSERT INTO song(id, id_song, song, track_time)
VALUES(7, 4, 'Easier to Run', '3:24');

INSERT INTO song(id, id_song, song, track_time)
VALUES(8, 4, 'Faint', '2:42');

INSERT INTO song(id, id_song, song, track_time)
VALUES(9, 5, 'Californication', '5:21');

INSERT INTO song(id, id_song, song, track_time)
VALUES(10, 5, 'I Could Have Lied (Live)', '4:26');

INSERT INTO song(id, id_song, song, track_time)
VALUES(11, 6, 'Desecration Smile', '5:02');

INSERT INTO song(id, id_song, song, track_time)
VALUES(12, 6, 'Wet Sand', '5:10');

INSERT INTO song(id, id_song, song, track_time)
VALUES(13, 7, 'R.E.M', '4:05');

INSERT INTO song(id, id_song, song, track_time)
VALUES(14, 7, 'God Is A Woman', '3:17');

INSERT INTO song(id, id_song, song, track_time)
VALUES(15, 8, 'Break Free Zedd', '3:35');

INSERT INTO song(id, id_song, song, track_time)
VALUES(16, 8, 'Hands on Me ASAP Ferg', '3:12');

INSERT INTO song(id, id_song, song, track_time)
VALUES(17, 9, 'Sour Candy', '2:38');

INSERT INTO song(id, id_song, song, track_time)
VALUES(18, 9, 'Sine From Above', '4:05');

INSERT INTO song(id, id_song, song, track_time)
VALUES(19, 10, 'Aura', '3:56');

INSERT INTO song(id, id_song, song, track_time)
VALUES(20, 10, 'Sexxx Dreams', '3:34');

INSERT INTO song(id, id_song, song, track_time)
VALUES(21, 11, 'Under a Blanket of Blue', '4:18');

INSERT INTO song(id, id_song, song, track_time)
VALUES(22, 11, 'The Nearness of You', '5:42');

INSERT INTO song(id, id_song, song, track_time)
VALUES(23, 12, 'Georgia On My Mind', '3:05');

INSERT INTO song(id, id_song, song, track_time)
VALUES(24, 12, 'That Meat and No Potatoes', '3:36');

INSERT INTO song(id, id_song, song, track_time)
VALUES(25, 13, 'Kinda Dukish', '2:33');

INSERT INTO song(id, id_song, song, track_time)
VALUES(26, 13, 'Passion Flower', '3:05');

INSERT INTO song(id, id_song, song, track_time)
VALUES(27, 14, 'Take the Coltrane', '4:44');

INSERT INTO song(id, id_song, song, track_time)
VALUES(28, 14, 'Big Nick', '4:29');

INSERT INTO song(id, id_song, song, track_time)
VALUES(29, 15, 'Chaconne From Partita No. 2 In D Minor', '15:12');

INSERT INTO song(id, id_song, song, track_time)
VALUES(30, 15, 'Double Violin Concerto', '18:14');

INSERT INTO song(id, id_song, song, track_time)
VALUES(31, 16, 'Variation 17 a 2 Clav. (1955 Version)', '0:53');

INSERT INTO song(id, id_song, song, track_time)
VALUES(32, 16, 'Variation 12. Canone alla Quarta (1955 Version)', '0:56');

INSERT INTO song(id, id_song, song, track_time)
VALUES(33, 17, 'Beggin', '2:50');

INSERT INTO song(id, id_song, song, track_time)
VALUES(34, 17, 'Candles', '2:48');

INSERT INTO song(id, id_song, song, track_time)
VALUES(35, 18, 'Vivaldi Summer Twist', '3:30');

INSERT INTO song(id, id_song, song, track_time)
VALUES(36, 18, 'Winter (from The Four Seasons)', '3:40');

INSERT INTO song(id, id_song, song, track_time)
VALUES(37, 19, 'Место', '4:04');

INSERT INTO song(id, id_song, song, track_time)
VALUES(38, 19, 'Слово к слову', '3:38');

INSERT INTO song(id, id_song, song, track_time)
VALUES(39, 20, 'Город дорог', '4:20');

INSERT INTO song(id, id_song, song, track_time)
VALUES(40, 20, 'Мутные замуты (remix)', '3:30');

INSERT INTO song(id, id_song, song, track_time)
VALUES(41, 21, 'Ушла', '3:40');

INSERT INTO song(id, id_song, song, track_time)
VALUES(42, 21, 'Нормально', '4:03');

INSERT INTO song(id, id_song, song, track_time)
VALUES(43, 22, 'Гуляй Рванина', '3:50');

INSERT INTO song(id, id_song, song, track_time)
VALUES(44, 22, 'Рашн сюр Бэнг', '3:39');


-- Создаем сборник
INSERT INTO compilacion(id, id_album , id_song, id_genre)
VALUES(1, 3, 5, 1);

INSERT INTO compilacion(id, id_album , id_song, id_genre)
VALUES(2, 15, 7, 2);

INSERT INTO compilacion(id, id_album , id_song, id_genre)
VALUES(3, 6, 20, 5);

INSERT INTO compilacion(id, id_album , id_song, id_genre)
VALUES(4, 6, 10, 3);

INSERT INTO compilacion(id, id_album , id_song, id_genre)
VALUES(5, 4, 19, 4);

INSERT INTO compilacion(id, id_album , id_song, id_genre)
VALUES(6, 7, 9, 3);

INSERT INTO compilacion(id, id_album , id_song, id_genre)
VALUES(7, 8, 15, 5);

INSERT INTO compilacion(id, id_album , id_song, id_genre)
VALUES(8, 9, 17, 3);
