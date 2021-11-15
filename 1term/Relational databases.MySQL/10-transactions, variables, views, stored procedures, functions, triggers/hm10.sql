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

CREATE TABLE email(
	user_id BIGINT UNSIGNED NOT NULL,
	email VARCHAR(120) UNIQUE NOT NULL,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);

CREATE TABLE address(
	city_id  SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	address VARCHAR(120) UNIQUE NOT NULL,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);

CREATE TABLE city(
	city_id SERIAL,
	country_id BIGINT UNSIGNED NOT NULL,
	city VARCHAR(120) UNIQUE NOT NULL,
    	FOREIGN KEY (city_id) REFERENCES address(city_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (country_id)
);

CREATE TABLE country(
	country_id SERIAL,
	country VARCHAR(120) UNIQUE NOT NULL,
    	FOREIGN KEY (country_id) REFERENCES address(country_id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE invoice(
	invoice_id SERIAL,
	users_id BIGINT UNSIGNED NOT NULL,
	invoice VARCHAR(120) UNIQUE,
	summa DECIMAL(10, 2)  NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);

CREATE TABLE payment(
	payment_id SERIAL,
	users_id BIGINT UNSIGNED NOT NULL,
	payment VARCHAR(120) UNIQUE,
	summa DECIMAL(10, 2)  NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    	FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);

CREATE TABLE payment_method(
	payment__method_id SERIAL,
	payment_id BIGINT UNSIGNED NOT NULL,
	payment_method VARCHAR(120) UNIQUE,
    	FOREIGN KEY (payment_id) REFERENCES payment(payment_id) ON UPDATE CASCADE ON DELETE RESTRICT, 
	INDEX (user_id)
);

accounts
connections