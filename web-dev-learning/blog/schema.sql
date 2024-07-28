DROP TABLE IF EXISTS posts;  
-- deletes any already existing tables named posts so you don’t get confusing behavior

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);