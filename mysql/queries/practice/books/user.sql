SELECT * FROM books.users;
INSERT INTO users (first_name,last_name)
VALUES ('Jane','Amsden'),
('Emily','Dixon'),
('Thepdore','Dostoevsky'),
('William','Shapiro'),
('Lao','Xiu');
UPDATE users
SET first_name='Bill'
WHERE id=4;