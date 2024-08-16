import os
from flask import Flask, render_template, redirect, request, url_for, flash

import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_secret_key'

# MySQL database configuration
if os.getenv('ClearDB env', 'FALSE') == 'TRUE':
    print('Database Running in clearDB...')
    DB_HOST = 'db'
    DB_USER = 'dbmaster'
    DB_PASSWORD = ''
    DB_DATABASE = 'blogdb'
else:
    print('Database Running in local env....')
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWORD = 'password'  # update to your MySQL database password
    DB_DATABASE = 'blogdb'

# Function to get database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
    cursor = connection.cursor(dictionary=True)
    return connection, cursor


# Route for the home page
@app.route('/')
def home():
    connection, cursor = get_db_connection()
    cursor.execute('SELECT * FROM postsTable ORDER BY created_at DESC')
    posts = cursor.fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Route to create a new blog post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        connection, cursor = get_db_connection()
        cursor.execute('INSERT INTO postsTable (title, content) VALUES (%s, %s)', (title, content))
        connection.commit()
        connection.close()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('create_post.html')

# Route to read a single blog post
@app.route('/post/<int:id>')
def read_post(id):
    connection, cursor = get_db_connection()
    cursor.execute('SELECT * FROM postsTable WHERE id = %s', (id,))
    post = cursor.fetchone()
    connection.close()
    return render_template('read_post.html', post=post)

# Route to update an existing blog post
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_post(id):
    connection, cursor = get_db_connection()
    cursor.execute('SELECT * FROM postsTable WHERE id = %s', (id,))
    post = cursor.fetchone()
    connection.close()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        connection, cursor = get_db_connection()
        cursor.execute('UPDATE postsTable SET title = %s, content = %s WHERE id = %s', (title, content, id))
        connection.commit()
        connection.close()
        
        flash('Post updated successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('update_post.html', post=post)

# Route to delete a blog post
@app.route('/delete/<int:id>', methods=['POST'])
def delete_post(id):
    connection, cursor = get_db_connection()
    cursor.execute('DELETE FROM postsTable WHERE id = %s', (id,))
    connection.commit()
    connection.close()
    
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
