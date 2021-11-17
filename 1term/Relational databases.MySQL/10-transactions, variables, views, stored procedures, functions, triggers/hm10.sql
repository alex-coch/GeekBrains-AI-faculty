/* 
Ѕаза данных »нтернет-провайдера, решаемые задачи по учету:
- клиентов
- услуг
- счетов и их оплат
- биллинга
*/ 
DROP DATABASE example;
CREATE DATABASE example;
USE example;
CREATE TABLE users(
	user_id SERIAL,
	firstname VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL,
	phone CHAR(11) NOT NULL,	
	password_hash CHAR(65), 
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	INDEX (user_id),
	INDEX (lastname),
	INDEX (phone)
);
INSERT INTO `users` (`user_id`, `firstname`, `lastname`, `phone`, `password_hash`, `created_at`, `updated_at`) VALUES (NULL, 'alex', 'coch', '123456789', 'pass_hash', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

CREATE TABLE email(
	user_id BIGINT UNSIGNED NOT NULL,
	email VARCHAR(120) UNIQUE NOT NULL,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);
INSERT INTO `email` (`user_id`, `email`) VALUES ('1', 'a@a.a');

CREATE TABLE address(
	city_id  SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	address VARCHAR(120) UNIQUE NOT NULL,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);
INSERT INTO `address` (`city_id`, `user_id`, `address`) VALUES (NULL, '1', 'in the middle of nowhere');

CREATE TABLE city(
	city_id SERIAL,
	country_id BIGINT UNSIGNED NOT NULL,
	city VARCHAR(120) UNIQUE NOT NULL,
    	FOREIGN KEY (city_id) REFERENCES address(city_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (country_id)
);
INSERT INTO `city` (`city_id`, `country_id`, `city`) VALUES ('1', '1', 'sometown');

CREATE TABLE country(
	country_id SERIAL,
	country VARCHAR(120) UNIQUE NOT NULL,
    	FOREIGN KEY (country_id) REFERENCES city(country_id) ON UPDATE CASCADE ON DELETE RESTRICT
);
INSERT INTO `country` (`country_id`, `country`) VALUES ('1', 'somecountry');

CREATE TABLE invoice(
	invoice_id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	invoice VARCHAR(120) UNIQUE,
	summa DECIMAL(10, 2)  NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);
INSERT INTO `invoice` (`invoice_id`, `user_id`, `invoice`, `summa`, `created_at`) VALUES (NULL, '1', 'smth', '1.0', CURRENT_TIMESTAMP);

CREATE TABLE payment(
	payment_id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	payment VARCHAR(120) UNIQUE,
	summa DECIMAL(10, 2)  NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);
INSERT INTO `payment` (`payment_id`, `user_id`, `payment`, `summa`, `created_at`) VALUES (NULL, '1', 'smth2', '0.5', CURRENT_TIMESTAMP);

CREATE TABLE payment_method(
	payment__method_id SERIAL,
	payment_id BIGINT UNSIGNED NOT NULL,
	payment_method VARCHAR(120) UNIQUE,
    	FOREIGN KEY (payment_id) REFERENCES payment(payment_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (payment_id)
);
INSERT INTO `payment_method` (`payment__method_id`, `payment_id`, `payment_method`) VALUES (NULL, '1', 'card');

CREATE TABLE account(
	account_id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	account VARCHAR(120),
	summa DECIMAL(10, 2) NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);
INSERT INTO `account` (`account_id`, `user_id`, `account`, `summa`, `created_at`) VALUES (NULL, '1', 'voip', '2.0', CURRENT_TIMESTAMP);

CREATE TABLE connection (
	connection_id  SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	ip VARCHAR(20) NOT NULL,
	start_time DATETIME NOT NULL,
	finish_time DATETIME NOT NULL,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);
INSERT INTO `connection` (`connection_id`, `user_id`, `ip`, `start_time`, `finish_time`) VALUES (NULL, '1', '2.2.2.2', '2021-11-16 14:53:46', '2021-11-16 14:55:46');

CREATE VIEW cat AS SELECT concat(users.firstname, ' ', users.lastname) AS name, (SELECT payment_method FROM payment_method WHERE payment_id = payment.payment_id) as payment_method, sum(summa) AS total FROM users JOIN payment ON users.user_id = payment.user_id GROUP BY name, payment_method;
SELECT * FROM cat;

CREATE VIEW inv AS SELECT concat(users.firstname, ' ', users.lastname) AS name, invoice, summa FROM users JOIN invoice ON users.user_id = invoice.user_id;
SELECT * FROM inv;

DELIMITER //
DROP PROCEDURE IF EXISTS get_conn //
CREATE PROCEDURE get_conn(OUT total INT)
-- DETERMINISTIC
READS SQL DATA
BEGIN
    SELECT count(*) INTO total FROM connection;
END //
CALL get_conn(@total) //
SELECT @total //

delimiter $$
DROP TRIGGER IF EXISTS foo $$
create trigger foo before insert on users
for each row
begin
	IF (new.password_hash IS NULL) then 
    	signal sqlstate '45000';
    END IF;
END $$
INSERT INTO `users` (`user_id`, `firstname`, `lastname`, `phone`, `password_hash`, `created_at`, `updated_at`) VALUES (NULL, 'a', 'b', '1', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)

