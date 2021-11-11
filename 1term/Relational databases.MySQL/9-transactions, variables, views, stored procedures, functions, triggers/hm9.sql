-- 1
START TRANSACTION; 
INSERT INTO sample.users SELECT * FROM shop.users WHERE id=1;
COMMIT;

-- 2
CREATE VIEW cat AS SELECT products.name, catalogs.name FROM `products` JOIN catalogs ON catalogs.id=products.catalog_id; 
SELECT * FROM cat;

--3
SELECT created_at, IF (created_at BETWEEN '2018-08-01' AND '2018-08-30', '1', '0') AS x FROM users;

--4
prepare stmt from "delete from users order by created_at limit ?";
set @cnt=(select count(1)-5 from users);
execute stmt using @cnt;

-- 1 ?
DROP USER IF EXISTS 'shop'@'localhost';
DROP USER IF EXISTS 'shop_read'@'localhost';
DELETE FROM mysql.user WHERE user LIKE 'shop%';
SELECT user FROM mysql.user;
FLUSH PRIVILEGES;
CREATE USER 'shop'@'localhost' IDENTIFIED BY 'pass1';
CREATE USER 'shop_read'@'localhost' IDENTIFIED BY 'pass2';
GRANT ALL ON shop.* TO 'shop';
GRANT SELECT ON shop.* TO 'shop_read';

--2?

--1 
DELIMITER //
DROP FUNCTION IF EXISTS hello //
CREATE FUNCTION hello()
RETURNS text
DETERMINISTIC
READS SQL DATA
BEGIN
	SET @hour1 = HOUR(now());
	CASE 
    WHEN (@hour1 >= 6 AND @hour1 < 12) THEN RETURN 'Good morning';
	WHEN (@hour1 >= 12 AND @hour1 < 18) THEN RETURN 'Good day';
    ELSE RETURN 'Good night';
    END CASE;
END //
SELECT hello() //