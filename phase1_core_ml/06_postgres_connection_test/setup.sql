DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  score INT NOT NULL
);
INSERT INTO students (name, score) VALUES
('Alice',88),('Bob',92),('Charlie',79);
