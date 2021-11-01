/*  Уќператоры, фильтраци€, сортировка и ограничениеФ */
/*1*/
ALTER TABLE users ADD updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP;
UPDATE users SET created_at=NOW();

/*2*/
UPDATE users SET created_at=DATE_FORMAT(STR_TO_DATE(created_at, '%e.%c.%Y %H:%i'), '%Y-%m-%d %H:%m:%s'), updated_at=DATE_FORMAT(STR_TO_DATE(updated_at, '%e.%c.%Y %H:%i'), '%Y-%m-%d %H:%m:%s');

/*3*/
SELECT * FROM storehouses_products ORDER BY CASE WHEN value = 0 THEN 2147483647 ELSE value END;

/*4*/
SELECT * FROM profiles WHERE LOWER(MONTHNAME(birthday)) in ('may', 'august') 

/*5*/
SELECT * FROM catalogs WHERE id IN (5, 1, 2) ORDER BY FIELD(ID,5,1,2) 

/* Ујгрегаци€ данныхФ */
/*1*/
SELECT AVG(TIMESTAMPDIFF(YEAR, birthday, NOW())) FROM `profiles` JOIN users ON users.id = profiles.user_id 

/*2*/
SELECT DAYOFWEEK(birthday) AS day, count(*) FROM `profiles` GROUP BY day

/*3*/
select ROUND(exp(sum(ln(id))), 0) from users

