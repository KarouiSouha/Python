SELECT * FROM dojos_and_ninjas.dojos;
SELECT * FROM dojos_and_ninjas.dojos;
INSERT INTO dojos (name)
VALUES ('Swift Fist Dojo'),
('Rising Sun Dojo'),
('Zen Harmony Dojo');
DELETE FROM dojos WHERE id IN (1,2,3) ;
INSERT INTO dojos (name)
VALUES ('Phoenix Martial Arts Studio'),
('Iron Mountain Dojo'),
('Golden Tiger Training Center');
ALTER  TABLE dojos auto_increment = 0