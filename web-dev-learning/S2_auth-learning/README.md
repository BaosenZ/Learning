# Authentication and authrization Learning

- The Auth can be implemented without session, hash function, database
  However, this method is not safe. 

- Use session

- Use Flask-Login to simplify session

- Use bcrypt and env to protect password

- Use database
It is not necessary to use database for one admin. But if we want to deploy the app and update the blogs, we need incorpate the database to store and manage the blogs. 
If we want to add "register", the database is also needed.
