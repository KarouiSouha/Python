SELECT * FROM dojos_and_ninjas.ninjas;
INSERT INTO ninjas (first_name,last_name,age, dojos_id) VALUES
    ('Kenji','Takahashi',20,4),
    ('Ayako','Nakamura',30, 4),
    ('Hiroshi','Tanaka',23, 4);
INSERT INTO ninjas (first_name,last_name,age, dojos_id) VALUES
    ('Emi ','Suzuki',20,5),
    ('Kaito','Yamamoto',30, 5),
    ('Mei','Nakajima',23, 5);
INSERT INTO ninjas (first_name,last_name,age, dojos_id) VALUES
    ('Kazuki','Sato',20,6),
    ('Yumi','Ito',30, 6),
    ('Riku','Kawasaki',23, 6);
SELECT * FROM ninjas WHERE dojos_id = 4;
SELECT * FROM ninjas WHERE dojos_id = (SELECT MAX(id) FROM dojos);
SELECT name AS dojo_name
FROM dojos
WHERE id = (
    SELECT dojos_id
    FROM ninjas
    ORDER BY id DESC
    LIMIT 1
);

