CREATE DATABASE blogs_sort_demo;

USE blogs_sort_demo;

CREATE TABLE blogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    sort_order INT DEFAULT 0
);

INSERT INTO blogs (title, content, sort_order) VALUES 
('First Blog Post', 'This is the content of the first blog post.', 1),
('Second Blog Post', 'This is the content of the second blog post.', 2),
('Third Blog Post', 'This is the content of the third blog post.', 3);