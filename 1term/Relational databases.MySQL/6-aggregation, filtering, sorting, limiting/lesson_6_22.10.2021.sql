/*
 * 
 * Запрос 1. Выбираем основную информацию пользователя с id=1.
*/


-- Выбираем данные пользователя с id 1

SELECT
	firstname,
	lastname,
	'city', 
	'profile_photo'
FROM users
WHERE id = 1;

-- находим город
SELECT city FROM profiles WHERE user_id = 1;

-- добавляем подзапрос, который выводит город

SELECT
	firstname,
	lastname,
	(SELECT city FROM profiles WHERE user_id = 1) AS city, 
	'profile_photo'
FROM users
WHERE id = 1;

-- находим id фотографии профиля
SELECT photo_id FROM profiles WHERE user_id = 1;

-- находим имя файла
SELECT file_name FROM media WHERE id = 1;

-- находим имя файла с id фотографии профиля
SELECT file_name FROM media WHERE id = (SELECT photo_id FROM profiles WHERE user_id = 1);

-- добавляем подзапрос, который выводит имя файла
SELECT
	firstname,
	lastname,
	(SELECT city FROM profiles WHERE user_id = 1) AS city, 
	(SELECT file_name FROM media WHERE id = (SELECT photo_id FROM profiles WHERE user_id = 1)) AS profile_photo
FROM users
WHERE id = 1;

-- Ссылаемся на id извне
SELECT
	firstname,
	lastname,
	(SELECT city FROM profiles WHERE user_id = users.id) AS city, 
	(SELECT file_name FROM media WHERE id = (SELECT photo_id FROM profiles WHERE user_id = users.id)) AS profile_photo
FROM users
WHERE id = 1;

/*
 * Задание 2. Поиск медиафайлов пользователя с id = 1.
*/
-- Ищем все картинки пользователя

SELECT * FROM media WHERE user_id = 1 AND media_types_id = 1;

SELECT id FROM media_types WHERE name = 'image';

SELECT * FROM media WHERE user_id = 1 AND media_types_id = (SELECT id FROM media_types WHERE name = 'image');

-- если не знаем id пользователя
SELECT id FROM users WHERE email = 'greenfelder.antwan@example.org';

SELECT * FROM media WHERE user_id = (SELECT id FROM users WHERE email = 'greenfelder.antwan@example.org') 
	AND media_types_id = (SELECT id FROM media_types WHERE name = 'image');

SELECT * FROM media 
	WHERE 
		user_id = (SELECT id FROM users WHERE email = 'greenfelder.antwan@example.org') 
		AND media_types_id = (SELECT id FROM media_types WHERE name = 'image') 
		AND file_size > 10;

-- если хотим вывести только *.png
SELECT * FROM media WHERE 
	user_id = (SELECT id FROM users WHERE email = 'greenfelder.antwan@example.org') 
	AND media_types_id = (SELECT id FROM media_types WHERE name = 'image')
	AND file_name LIKE '%.png';
	
-- если хотим вывести только *.png и *.jpg
SELECT * 
FROM media
WHERE user_id = (SELECT id FROM users WHERE email = 'greenfelder.antwan@example.org')
AND (file_name LIKE '%.png' OR file_name LIKE '%.jpg');

/*
 * Задание 3. Посчитаем количество медиафайлов каждого типа.
*/
-- количество всех файлов в таблице media
SELECT COUNT(*) FROM media;

-- количество файлов с группировкой по типу
SELECT COUNT(*), media_types_id FROM media GROUP BY media_types_id;

-- количество файлов с группировкой по типу и называнием типа файла
SELECT COUNT(*) AS cnt, (SELECT name FROM media_types WHERE id = media_types_id) AS media_type
FROM media GROUP BY media_types_id;


/*
 * Задание 4. Посчитаем количество медиафайлов каждого типа для каждого пользователя.
*/

SELECT * FROM media;

SELECT COUNT(*) AS cnt, (SELECT name FROM media_types WHERE id = media_types_id) AS media_type, user_id
	FROM media
	GROUP BY media_types_id, user_id
	ORDER BY user_id;

/*
 * Задание 5. Выбираем друзей пользователя с id = 1.
 * 
*/


-- выбираем кому пользователь отправил заявки
SELECT to_user_id FROM friend_requests WHERE from_user_id = 1 AND request_type = 1;

-- выбираем кому пользователь отправил заявки, заявки приняты
SELECT from_user_id FROM friend_requests WHERE to_user_id = 1 AND request_type = 1;

-- объединяем две группы, чтобы получить всех друзей
SELECT to_user_id FROM friend_requests WHERE from_user_id = 1 AND request_type = 1
UNION
SELECT f

-- "развёрнутый" вариант следующего запроса с колонкой, где проверяется to_user_id = 1
SELECT *, (to_user_id = 1), IF(to_user_id = 1, from_user_id, to_user_id) AS friend  FROM friend_requests
WHERE request_type = 1 AND (from_user_id = 1 OR to_user_id = 1);

-- еще один вариант без использования UNION
SELECT DISTINCT IF(to_user_id = 1, from_user_id, to_user_id) AS friend  FROM friend_requests
WHERE request_type = 1 AND (from_user_id = 1 OR to_user_id = 1);

/*
 * Задание 6. Выводим имя и фамилию друзей пользователя с id = 1
*/

-- здесь 2, 3, 5, 7, 11 - это "заглушка"
SELECT CONCAT(firstname,' ', lastname) AS name FROM users WHERE id IN (2, 3, 5, 7, 11);

SELECT CONCAT(firstname,' ', lastname) AS name FROM users WHERE id IN (
	SELECT to_user_id FROM friend_requests WHERE from_user_id = 1 AND 
		request_type = (SELECT id FROM friend_requests_types WHERE name = 'accepted')
	UNION
	SELECT from_user_id FROM friend_requests WHERE to_user_id = 1 AND 
		request_type = (SELECT id FROM friend_requests_types WHERE name = 'accepted'));
-- получаем тип дружбы по названию
SELECT id FROM friend_requests_types WHERE name = 'accepted';

-- введем переменную для сохранения результата поиска айди типа дружбы accepted
SET @request_id := (SELECT id FROM friend_requests_types WHERE name = 'accepted');
SELECT @request_id;

-- используем переменную в запросе
SELECT CONCAT(firstname,' ', lastname) AS name FROM users WHERE id IN (
	SELECT to_user_id FROM friend_requests WHERE from_user_id = 1 AND 
		request_type = @request_id
	UNION
	SELECT from_user_id FROM friend_requests WHERE to_user_id = 1 AND 
		request_type = @request_id);
		
/*
 * Задание 7. Выводим красиво информацию о друзьях. Выводим пол, возраст.
*/
-- выводим пол
SELECT 
	CASE (gender)
		WHEN 'f' THEN 'female'
		WHEN 'm' THEN 'male'
		WHEN 'x' THEN 'not defined'
	END AS gender 
FROM profiles;

-- выводим возраст
SELECT TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age FROM profiles;


SELECT CONCAT(firstname,' ', lastname) AS name, 
(SELECT TIMESTAMPDIFF(YEAR, birthday, NOW()) FROM profiles WHERE user_id = users.id) AS age,
(SELECT CASE (gender)
		WHEN 'f' THEN 'female'
		WHEN 'm' THEN 'male'
		WHEN 'x' THEN 'not defined'
	END FROM profiles WHERE user_id =  users.id) AS gender
FROM users WHERE id IN (
	SELECT to_user_id FROM friend_requests WHERE from_user_id = 1 AND 
		request_type = (SELECT id FROM friend_requests_types WHERE name = 'accepted')
	UNION
	SELECT from_user_id FROM friend_requests WHERE to_user_id = 1 AND 
		request_type = (SELECT id FROM friend_requests_types WHERE name = 'accepted'));

	
/*
 * Задание 8. Выводим все непрочитанные сообщения пользователя с id = 1.
*/
-- выводим все сообщения пользователя, сортируем по дате

SELECT * FROM messages WHERE from_user_id = 1 OR to_user_id = 1 ORDER BY created_at DESC;

-- выводим все непрочитанные сообщения из диалогов
SELECT * FROM messages 
WHERE (from_user_id = 1 OR to_user_id = 1) AND is_delivered = FALSE ORDER BY created_at DESC;

-- выводим все непрочитанные сообщения из диалогов
SELECT *, (from_user_id = 1) AS unread FROM messages 
WHERE (from_user_id = 1 OR to_user_id = 1)  AND is_delivered = FALSE ORDER BY unread, created_at DESC;

-- выводим сверху непрочитанные сообщения пользователя
SELECT * FROM messages 
WHERE (from_user_id = 1 OR to_user_id = 1)  AND is_delivered = FALSE ORDER BY from_user_id = 1, created_at DESC;