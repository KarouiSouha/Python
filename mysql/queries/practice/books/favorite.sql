SELECT * FROM books.favorites;
INSERT INTO favorites (users_id, books_id)
VALUES (1, 1), (1, 2);
INSERT INTO favorites (users_id, books_id)
VALUES (2, 1), (2, 2), (2, 3);
INSERT INTO favorites (users_id,books_id)
VALUES (3,1),(3,2),(3,3),(3,4);
INSERT INTO favorites (users_id, books_id)
VALUES (4, 1), (4, 2), (4, 3), (4, 4), (4, 5);
SELECT users.first_name, users.last_name FROM users
JOIN favorites ON users.id = users_id
JOIN books ON favorites.books_id = books.id
WHERE books.id = 3;
DELETE FROM favorites
WHERE books_id = 3 AND users_id = 1;
INSERT INTO favorites (users_id, books_id) 
VALUES (5, 2);
SELECT title from books
JOIN favorites  on favorites.books_id = books.id
WHERE favorites.users_id = 3;


SELECT first_name , last_name from users
JOIN favorites  on favorites.users_id = users.id
WHERE favorites.books_id = 5;
