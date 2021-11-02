/*1*/
SELECT (SELECT CONCAT(firstname, ' ', lastname) FROM users WHERE id = from_user_id), from_user_id, count(*) AS amount FROM `messages` JOIN users ON users.id=messages.from_user_id OR users.id=messages.to_user_id WHERE to_user_id=1 GROUP BY from_user_id ORDER BY amount DESC LIMIT 1;

/*2*/
SELECT count(likes.id) FROM profiles JOIN media ON profiles.user_id=media.user_id JOIN likes ON likes.media_id=media.id WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) < 10;

/*3*/
SELECT CASE (gender) WHEN 'f' THEN 'female' WHEN 'm' THEN 'male' WHEN 'x' THEN 'not defined' END AS gen, count(gender) AS amount FROM profiles JOIN media ON profiles.user_id=media.user_id JOIN likes ON likes.media_id=media.id GROUP BY gen ORDER BY amount DESC 