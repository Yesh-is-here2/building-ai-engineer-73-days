CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT,
  score INTEGER
);

INSERT INTO students VALUES
(1,'Alice',88),
(2,'Bob',92),
(3,'Charlie',79);

SELECT * FROM students WHERE score >= 85 ORDER BY score DESC;
