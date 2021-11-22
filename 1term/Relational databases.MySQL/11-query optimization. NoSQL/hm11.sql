-- 1
DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	id SERIAL,
  	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	table_name VARCHAR(20) NOT NULL,
	field_id BIGINT UNSIGNED NOT NULL,
	field_name VARCHAR(255)
	) ENGINE=ARCHIVE;

DELIMITER //

DROP TRIGGER IF EXISTS users_logs //
CREATE TRIGGER users_logs AFTER INSERT ON users
FOR EACH ROW
BEGIN
  INSERT INTO logs (table_name, field_id, `field_name`) VALUES ('users', NEW.id, NEW.name);
END//

DROP TRIGGER IF EXISTS catalogs_logs //
CREATE TRIGGER catalogs_logs AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
  INSERT INTO logs (table_name, field_id, `field_name`) VALUES ('catalogs', NEW.id, NEW.name);
END//

DROP TRIGGER IF EXISTS products_logs //
CREATE TRIGGER products_logs AFTER INSERT ON products
FOR EACH ROW
BEGIN
  INSERT INTO logs (table_name, field_id, `field_name`) VALUES ('products', NEW.id, NEW.name);
END//

-- 2
DROP PROCEDURE IF EXISTS insert_into_users ;
delimiter //
CREATE PROCEDURE insert_into_users ()
BEGIN
	DECLARE i INT DEFAULT 1000000;
	DECLARE j INT DEFAULT 0;
	WHILE i > 0 DO
		INSERT INTO users(name, birthday_at) VALUES (CONCAT('user_', j), NOW());
		SET j = j + 1;
		SET i = i - 1;
	END WHILE;
END //
delimiter ;

CALL insert_into_users();


-- 1
HMSET admin1 login "user1" ip_addr "1.1.1.1" amount 0
HGETALL admin1

-- 2
hset user_email name email
hset email_user email name

hget user_email "name" 
hget email_user "email" 

--3
shop.catalogs.insertMany( [
      { _id: 1, name: "Процессоры"},
      { _id: 2, name: "Материнские платы"},
      { _id: 3 ,name: "Видеокарты"}
   ] );

shop.products.insert({
    name: "Intel Core i3-8100",
    description: "Процессор для настольных персональных компьютеров, основанных на платформе Intel.",
    price: 7890.00,
    catalog: 1
})