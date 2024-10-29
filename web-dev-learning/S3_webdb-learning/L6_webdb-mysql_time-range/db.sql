CREATE DATABASE linkedin_demo;

USE linkedin_demo;

CREATE TABLE experiences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE,
    is_present BOOLEAN DEFAULT FALSE
);
