# MySQL learning

For local host: start mysql command line clint, enter password (root, your password), start mysql workbench. start your work on database...
(if client cannot start, go to Windows service and start manully. See this link: https://medium.com/@aditya4567uk/error-solved-mysql-client-not-opening-mysql80-service-error-d94aeaee64b5#:~:text=Firstly%20just%20go%20your%20search%20area%20by,start%20the%20required%20backend%20services%20of%20MySQL)

find ip address in mysql workbench: "database > management connections"\

`show databases;`\
`create database <name>;`\
`DROP DATABASE <database-name>;`\
`USE <database-name>;`\


Create Tables:
```
CREATE TABLE cats (
    name VARCHAR(50),
    age INT
);
 
CREATE TABLE dogs (
    name VARCHAR(50),
    breed VARCHAR(50),
    age INT
);
```

`SHOW tables;`
`SHOW COLUMNS FROM cats;`
`DESC cats;`
`DROP TABLE <table-name>;`

Insert a cat to cats Table:
```
INSERT INTO cats (name, age) 
VALUES ('Blue Steele', 5);
```

To view all rows in our table:
`SELECT * FROM cats;`

Multiple Insert:
```
INSERT INTO cats (name, age) 
VALUES 
  ('Meatball', 5), 
  ('Turkey', 1), 
  ('Potato Face', 15);
```

Using NOT NULL:
```
CREATE TABLE cats2 (
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);
```

Using single quote for text.

Define a table with a DEFAULT name:
```
CREATE TABLE cats3  (    
    name VARCHAR(20) DEFAULT 'no name provided',    
    age INT DEFAULT 99  
);
```

Combine NOT NULL and DEFAULT:
```
CREATE TABLE cats4  (    
    name VARCHAR(20) NOT NULL DEFAULT 'unnamed',    
    age INT NOT NULL DEFAULT 99 
);
```

Row identifier and primary key:
```
CREATE TABLE unique_cats (
	cat_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);
```
Another way:
```
CREATE TABLE unique_cats2 (
	cat_id INT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (cat_id)
);
```

Auto-increment ID using AUTO_INCREMENT:
```
CREATE TABLE unique_cats3 (
    cat_id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (cat_id)
);
```

More about `SELECT`: 
To get all the columns: `SELECT * FROM cats;`
To only get the age column: `SELECT age FROM cats;`
To select multiple specific columns: `SELECT name, breed FROM cats;`

Use where to specify a condition: 
`SELECT * FROM cats WHERE age = 4;`
`SELECT * FROM cats WHERE name ='Egg';`

Use 'AS' to alias a column in your results (it doesn't actually change the name of the column in the table):
`SELECT cat_id AS id, name FROM cats;`

Updating Data (Try SELECT before UPDATE to check if we update right): `UPDATE cats SET breed='Shorthair' WHERE breed='Tabby';`

Delete all cats with name of 'Egg': `DELETE FROM cats WHERE name='Egg';`
Delete all rows in the cats table: `DELETE FROM cats;`