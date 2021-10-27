/* 1 */
SELECT (SELECT CONCAT(firstname, ' ', lastname) FROM users WHERE id = from_user_id), count(*) AS AMOUNT FROM `messages` WHERE `to_user_id` = 1 GROUP BY from_user_id ORDER BY AMOUNT DESC LIMIT 1

/* 2 */
SELECT count(*) FROM `likes` JOIN profiles ON likes.user_id = profiles.user_id WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) > 18

/* 3 */
SELECT CASE (gender) WHEN 'f' THEN 'female' WHEN 'm' THEN 'male' WHEN 'x' THEN 'not defined' END AS GEN, count(*) AS AMOUNT FROM `likes` JOIN profiles ON likes.user_id = profiles.user_id GROUP BY GEN