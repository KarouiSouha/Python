SELECT * FROM books.books;
INSERT INTO books(title,num_of_pages)
VALUES ('C Sharp',200),
('Java',250),
('Python',350),
('PHP',100),
('Ruby',270);
UPDATE Books
SET title = 'C#'
WHERE id=1;
