/*1*/
ALTER TABLE users ADD updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP;
UPDATE users SET created_at=NOW();

/*2*/
UPDATE users SET created_at=DATE_FORMAT(STR_TO_DATE(created_at, '%e.%c.%Y %H:%i'), '%Y-%m-%d %H:%m:%s'), updated_at=DATE_FORMAT(STR_TO_DATE(updated_at, '%e.%c.%Y %H:%i'), '%Y-%m-%d %H:%m:%s');

/*3*/
SELECT * FROM storehouses_products ORDER BY CASE WHEN value = 0 THEN 2147483647 ELSE value END;

