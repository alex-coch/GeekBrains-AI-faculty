/*1*/
SELECT name FROM `users` JOIN orders ON users.id=orders.user_id 

/*2*/
SELECT products.name, catalogs.name FROM `products` JOIN catalogs ON products.catalog_id=catalogs.id 

/*3*/
SELECT (SELECT name FROM cities WHERE label = flights.from1) AS from1, (SELECT name FROM cities WHERE label = flights.to1) AS to1 FROM `flights` 