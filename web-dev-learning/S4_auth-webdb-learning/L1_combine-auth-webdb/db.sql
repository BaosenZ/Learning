CREATE DATABASE IF NOT EXISTS mywebdb;

USE mywebdb;

CREATE TABLE projectsTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    label VARCHAR(100),
    start_date DATE NOT NULL,
    end_date DATE,
    is_present BOOLEAN DEFAULT FALSE,
    content TEXT NOT NULL,
    image LONGBLOB
);