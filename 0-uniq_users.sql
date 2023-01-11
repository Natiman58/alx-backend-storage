-- create a table called users
-- in the database holberton
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255),
    PRIMARY KEY (id)
);

