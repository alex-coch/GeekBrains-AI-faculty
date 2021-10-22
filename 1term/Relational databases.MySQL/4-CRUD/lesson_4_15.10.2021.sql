-- Поработаем с колонкой таблицы users, добавлением, модификацией, удалением

-- Добавим колонку с номером паспорта
ALTER TABLE users ADD COLUMN passport_number VARCHAR(10);
-- Изменим ее тип
ALTER TABLE users MODIFY COLUMN passport_number VARCHAR(20);
-- Переименуем ее
ALTER TABLE users RENAME COLUMN passport_number TO passport;
-- Добавим индекс на колонку
ALTER TABLE users ADD INDEX passport_idx (passport);
-- Удалим индекс
ALTER TABLE users DROP INDEX passport_idx;
-- Удалим колонку
ALTER TABLE users DROP COLUMN passport;

-- совершенствуем таблицу дружбы
-- добавляем ограничение, что отправитель запроса на дружбу 
-- не может быть одновременно и получателем

-- CHECK CONSTRAINTS

ALTER TABLE friend_requests ADD CONSTRAINT CHECK(from_user_id != to_user_id);

-- добавляем ограничение, что номер телефона должен состоять из 11
-- символов и только из цифр
-- https://regex101.com/
ALTER TABLE users ADD CONSTRAINT CHECK(REGEXP_LIKE(phone, '^[0-9]{11}$'));

-- делаем id photo пользователей уникальными
ALTER TABLE profiles MODIFY COLUMN photo_id BIGINT UNSIGNED DEFAULT NULL UNIQUE;

-- делаем foreign key на media
ALTER TABLE profiles ADD CONSTRAINT fk_profiles_media FOREIGN KEY (photo_id) REFERENCES media (id);

/* 
  C - Create = INSERT
  R - Read   = SELECT
  U - Update = UPDATE
  D - Delete = DELETE
*/

/*
 * INSERT
 * https://dev.mysql.com/doc/refman/8.0/en/insert.html
 */

DESCRIBE users;

-- добавляем пользователя
INSERT users (id, firstname, lastname, phone, email, password_hash, created_at, updated_at)
VALUES (DEFAULT, 'Alex', 'Stepanov', '89213546566','alex@mail.com','asdsdaasd', DEFAULT, DEFAULT);

SELECT * FROM users;

-- добавляем повторно того же пользователя, ошибка не возникает
INSERT IGNORE users (id, firstname, lastname, phone, email, password_hash, created_at, updated_at)
VALUES (DEFAULT, 'Alex', 'Stepanov', '89213546566','alex@mail.com','asdsdaasd', DEFAULT, DEFAULT);

-- не указываем default значения
INSERT users (firstname, lastname, phone, email, password_hash)
VALUES ('Lena', 'Stepanova', '89213546568', 'lena@mail.com', 'hjkhkjh' );

-- не указываем названия колонок
INSERT users 
VALUES (DEFAULT, 'Chris', 'Ivanov', '89213546560', 'chris@mail.com', 'kdfhgkasd', DEFAULT, DEFAULT);


-- явно задаем id
INSERT INTO users (id, firstname, lastname, email, phone) VALUES 
(55, 'Jane', 'Kvanov', 'jane@mail.com', '89293546560');

SELECT * FROM users;

-- пробуем добавить id меньше текущего
INSERT INTO users (id, firstname, lastname, email, phone) VALUES 
(45, 'Jane', 'Night', 'jane_n@mail.com', '89293946560');

-- добавляем несколько пользователей
INSERT INTO users (firstname, lastname, email, phone)
VALUES ('Igor', 'Petrov', 'igor@mail.com', '89213549560'),
       ('Oksana', 'Petrova', 'oksana@mail.com', '89213549561');
       
-- добавляем через SET
INSERT users
SET firstname = 'Iren',
    lastname = 'Sidorova',
    email = 'iren@mail.com',
    phone = '89213541560';
   
-- добавляем через SELECT
   
INSERT users (firstname, lastname, email, phone)
SELECT name, surname, email, phone FROM test1.users;

/*
 * SELECT
 * https://dev.mysql.com/doc/refman/8.0/en/select.html
 */

-- выбираем константы
SELECT 1;

SELECT 'Hello world!';

SELECT 10 + 1;

-- выбираем все поля users
SELECT * FROM users;

-- выбираем только имена users
SELECT firstname FROM users;

-- выбираем только уникальные имена
SELECT DISTINCT firstname FROM users;

-- выбираем пользователей, у которых нет hash пароля
SELECT * FROM users WHERE password_hash IS NULL;

-- выбираем пользователей, у которых есть hash пароля
SELECT * FROM users WHERE password_hash IS NOT NULL;

-- выбираем пользователей с именем Аноним
SELECT * FROM users WHERE firstname = 'Аноним';

-- выбираем пользователей с id больше или равным 85
SELECT * FROM users WHERE id >= 85;

-- выбираем пользователей с id больше или равным 85 и меньше или равным 100
SELECT * FROM users WHERE id >= 85 AND id <= 100;

-- аналогично предыдущему запросу
SELECT * FROM users WHERE id BETWEEN 85 AND 100;

-- выбираем столбцы с фамилией, именем и телефоном
SELECT lastname, firstname, phone FROM users;

-- соединяем имя и фамилию с помощью CONCAT, оставляет от имени только первую букву с помощью SUBSTR
-- задаем псевдоним username для столбца
SELECT CONCAT(lastname,' ', SUBSTR(firstname, 1, 1), '.') AS username, phone FROM users;

-- выбираем пользователя Екатерина с id c 70 по 100
SELECT * FROM users WHERE firstname = 'Екатерина' AND id >=70 AND id <=100;

-- выбираем пользователя с именем Екатерина или Аноним
SELECT * FROM users WHERE firstname = 'Екатерина' OR firstname = 'Аноним';

-- выбираем четырёх пользователей
SELECT * FROM users LIMIT 4;

-- выбираем 5 пользователей, пропускаем первых 10
SELECT * FROM users LIMIT 5 OFFSET 10;

-- аналогично предыдущему запросу
SELECT * FROM users LIMIT 10,5;

/*
 * UPDATE
 * https://dev.mysql.com/doc/refman/8.0/en/update.html 
*/
-- добавляем несколько сообщений
INSERT INTO messages (from_user_id, to_user_id, body)
VALUES (45, 55, 'Hi!');

INSERT INTO messages (from_user_id, to_user_id, body)
VALUES (45, 55, 'I hate you!');

SELECT * FROM messages;

-- меняем текст сообщения
UPDATE messages 
SET body = 'I love you'
WHERE id = 5;

-- меняем статус на сообщение доставлено
UPDATE messages 
SET is_delivered = 1;

/*
 * DELETE
 * https://dev.mysql.com/doc/refman/8.0/en/update.html 
 * TRUNCATE
 * https://dev.mysql.com/doc/refman/8.0/en/truncate-table.html
*/

SELECT * FROM users WHERE lastname = 'Stepanov';

-- удаляем пользователя с фамилией Степанов
DELETE FROM users WHERE lastname = 'Stepanov';

-- удаляем все строки из messages
DELETE FROM messages;
SELECT * FROM messages;

-- выбираем Ивановых 
SELECT * FROM users WHERE lastname = 'Иванов' OR lastname = 'Ivanov';

-- удаляем ивановых
DELETE FROM users WHERE lastname = 'Иванов' OR lastname = 'Ivanov';

-- Пытаемся удалить пользователя с id = 1
-- Но это не получится, так как есть информация, связанная с ним в дочерних таблицах (сообщения, сообщества и т.д)
DELETE FROM users WHERE id = 1;

SELECT * FROM communities_users;

-- Очищаем таблицу
TRUNCATE TABLE communities_users;