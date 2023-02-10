-- Ок вроде
-- заполнение жанр
INSERT INTO genre(id, genre)
VALUES(1, 'ROCK');

INSERT INTO genre(id, genre)
VALUES(2, 'POP');

INSERT INTO genre(id, genre)
VALUES(3, 'Jazz');

INSERT INTO genre(id, genre)
VALUES(4, 'Classic');

INSERT INTO genre(id, genre)
VALUES(5, 'RAP');

-- заполнение испотнители
INSERT INTO executors(id, name)
VALUES(1, 'Queen');

INSERT INTO executors(id, name)
VALUES(2, 'Linkin Park');

INSERT INTO executors(id, name)
VALUES(3, 'Red Hot Chili Peppers');

INSERT INTO executors(id, name)
VALUES(4, 'Ariana Grande');

INSERT INTO executors(id, name)
VALUES(5, 'Lady Gaga');

INSERT INTO executors(id, name)
VALUES(6, 'Louis Armstrong');

INSERT INTO executors(id, name)
VALUES(7, 'Duke Ellington');

INSERT INTO executors(id, name)
VALUES(8, 'Johann Sebastian Bach');

INSERT INTO executors(id, name)
VALUES(9, 'Antonio Vivaldi');

INSERT INTO executors(id, name)
VALUES(10, 'Centr');

INSERT INTO executors(id, name)
VALUES(11, 'Slim');

-- заполнение альбомов
INSERT INTO albums(id, album, year_output)
VALUES(1, 'Sheer Heart Attack', '1974');

INSERT INTO albums(id, album, year_output)
VALUES(2, 'A Night at the Opera', '1975');

INSERT INTO albums(id, album, year_output)
VALUES(3, 'Hybrid Theory', '2000');

INSERT INTO albums(id, album, year_output)
VALUES(4, 'Meteora', '2003');

INSERT INTO albums(id, album, year_output)
VALUES(5, 'Californication', '1999');

INSERT INTO albums(id, album, year_output)
VALUES(6, 'Stadium Arcadium', '2006');

INSERT INTO albums(id, album, year_output)
VALUES(7,'Sweetener', '2018');

INSERT INTO albums(id, album, year_output)
VALUES(8, 'My Everything', '2014');

INSERT INTO albums(id, album, year_output)
VALUES(9, 'MChromatica', '2020');

INSERT INTO albums(id, album, year_output)
VALUES(10, 'Artpop', '2013');

INSERT INTO albums(id, album, year_output)
VALUES(11, 'Ella and Louis', '1956');

INSERT INTO albums(id, album, year_output)
VALUES(12, 'Satchmo', '1958');

INSERT INTO albums(id, album, year_output)
VALUES(13, 'Piano Reflections', '1953');

INSERT INTO albums(id, album, year_output)
VALUES(14, 'Duke Ellington & John Coltrane', '1963');

INSERT INTO albums(id, album, year_output)
VALUES(15,'Violin Concertos', '1986');

INSERT INTO albums(id, album, year_output)
VALUES(16, 'The Goldberg Variations', '2007');

INSERT INTO albums(id, album, year_output)
VALUES(17, 'The Four Seasons', '1970');

INSERT INTO albums(id, album, year_output)
VALUES(18, 'Vivaldi', '1967');

INSERT INTO albums(id, album, year_output)
VALUES(19, 'Легенды про…Centr', '2011');

INSERT INTO albums(id, album, year_output)
VALUES(20, 'Качели', '2007');

INSERT INTO albums(id, album, year_output)
VALUES(21, 'GUSLI', '2017');

INSERT INTO albums(id, album, year_output)
VALUES(22, 'Вид на жизнь', '2022');

-- Добовка треков
INSERT INTO song(id, album_id, song, track_time)
VALUES(1, 1, 'Dear Friends', 69);

INSERT INTO song(id, album_id, song, track_time)
VALUES(2, 1, 'Brighton Rock', 311);

INSERT INTO song(id, album_id, song, track_time)
VALUES(3, 2, 'Sweet Lady', 311);

INSERT INTO song(id, album_id, song, track_time)
VALUES(4, 2, 'Death On Two Legs (Dedicated To...)', 224);

INSERT INTO song(id, album_id, song, track_time)
VALUES(5, 3, 'Enth E Nd', 360);

INSERT INTO song(id, album_id, song, track_time)
VALUES(6, 3, 'P5hng Me A*wy', 338);

INSERT INTO song(id, album_id, song, track_time)
VALUES(7, 4, 'Easier to Run', 324);

INSERT INTO song(id, album_id, song, track_time)
VALUES(8, 4, 'Faint', 162);

INSERT INTO song(id, album_id, song, track_time)
VALUES(9, 5, 'Californication', 321);

INSERT INTO song(id, album_id, song, track_time)
VALUES(10, 5, 'I Could Have Lied (Live)', 266);

INSERT INTO song(id, album_id, song, track_time)
VALUES(11, 6, 'Desecration Smile', 302);

INSERT INTO song(id, album_id, song, track_time)
VALUES(12, 6, 'Wet Sand', 310);

INSERT INTO song(id, album_id, song, track_time)
VALUES(13, 7, 'R.E.M', 245);

INSERT INTO song(id, album_id, song, track_time)
VALUES(14, 7, 'God Is A Woman', 197);

INSERT INTO song(id, album_id, song, track_time)
VALUES(15, 8, 'Break Free Zedd', 215);

INSERT INTO song(id, album_id, song, track_time)
VALUES(16, 8, 'Hands on Me ASAP Ferg', 192);

INSERT INTO song(id, album_id, song, track_time)
VALUES(17, 9, 'Sour Candy', 158);

INSERT INTO song(id, album_id, song, track_time)
VALUES(18, 9, 'Sine From Above', 245);

INSERT INTO song(id, album_id, song, track_time)
VALUES(19, 10, 'Aura', 236);

INSERT INTO song(id, album_id, song, track_time)
VALUES(20, 10, 'Sexxx Dreams', 214);

INSERT INTO song(id, album_id, song, track_time)
VALUES(21, 11, 'Under a Blanket of Blue', 254);

INSERT INTO song(id, album_id, song, track_time)
VALUES(22, 11, 'The Nearness of You', 342);

INSERT INTO song(id, album_id, song, track_time)
VALUES(23, 12, 'Georgia On My Mind', 285);

INSERT INTO song(id, album_id, song, track_time)
VALUES(24, 12, 'That Meat and No Potatoes', 216);

INSERT INTO song(id, album_id, song, track_time)
VALUES(25, 13, 'Kinda Dukish', 153);

INSERT INTO song(id, album_id, song, track_time)
VALUES(26, 13, 'Passion Flower', 185);

INSERT INTO song(id, album_id, song, track_time)
VALUES(27, 14, 'Take the Coltrane', 184);

INSERT INTO song(id, album_id, song, track_time)
VALUES(28, 14, 'Big Nick', 249);

INSERT INTO song(id, album_id, song, track_time)
VALUES(29, 15, 'Chaconne From Partita No. 2 In D Minor', 1992);

INSERT INTO song(id, album_id, song, track_time)
VALUES(30, 15, 'Double Violin Concerto', 1094);

INSERT INTO song(id, album_id, song, track_time)
VALUES(31, 16, 'Variation 17 a 2 Clav. (1955 Version)', 53);

INSERT INTO song(id, album_id, song, track_time)
VALUES(32, 16, 'Variation 12. Cmyanone alla Quarta (1955 Version)', 56);

INSERT INTO song(id, album_id, song, track_time)
VALUES(33, 17, 'Beggin', 170);

INSERT INTO song(id, album_id, song, track_time)
VALUES(34, 17, 'Candles', 168);

INSERT INTO song(id, album_id, song, track_time)
VALUES(35, 18, 'Vivaldi Summer Twist', 210);

INSERT INTO song(id, album_id, song, track_time)
VALUES(36, 18, 'Winter (from The Four Seasons)', 220);

INSERT INTO song(id, album_id, song, track_time)
VALUES(37, 19, 'Место', 244);

INSERT INTO song(id, album_id, song, track_time)
VALUES(38, 19, 'Слово к слову', 218);

INSERT INTO song(id, album_id, song, track_time)
VALUES(39, 20, 'Город дорог', 260);

INSERT INTO song(id, album_id, song, track_time)
VALUES(40, 20, 'Мутные замуты (remix)', 210);

INSERT INTO song(id, album_id, song, track_time)
VALUES(41, 21, 'Ушламой', 220);

INSERT INTO song(id, album_id, song, track_time)
VALUES(42, 21, 'Нормально', 243);

INSERT INTO song(id, album_id, song, track_time)
VALUES(43, 22, 'Гуляй Рванина', 230);

INSERT INTO song(id, album_id, song, track_time)
VALUES(44, 22, 'Рашн сюр Бэнг', 219);


-- Создаем сборник
INSERT INTO compilation(id_compilation, names, year_output)
VALUES(1, 'Energy', 2003);

INSERT INTO compilation(id_compilation, names, year_output)
VALUES(2, 'Relax', 2018);

INSERT INTO compilation(id_compilation, names, year_output)
VALUES(3, 'Jazz Fun', 1956);

INSERT INTO compilation(id_compilation, names, year_output)
VALUES(4, 'Sunny Rock', 2018);

INSERT INTO compilation(id_compilation, names, year_output)
VALUES(5, 'Blue Fish', 2020);

INSERT INTO compilation(id_compilation, names, year_output)
VALUES(6, 'Retro',2010);

INSERT INTO compilation(id_compilation, names, year_output)
VALUES(7, 'Dance', 2022);

INSERT INTO compilation(id_compilation, names, year_output)
VALUES(8, 'FAN bounce', 2023);

INSERT INTO compilation(id_compilation, names, year_output)
VALUES(9, 'Попса+', 2004);
