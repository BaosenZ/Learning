CREATE DATABASE IF NOT EXISTS blogdb;

USE blogdb;

CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  email VARCHAR(50)
);