import os
from dotenv import load_dotenv
# flask app
from flask import Flask, render_template, redirect, request, url_for, flash
# database
import mysql.connector
# login
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import bcrypt
# display image data in database
import base64


# Load environment variables from .env file
load_dotenv()

# Init Flask App
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY

########## Database Init Start ##########
# MySQL database configuration
CLEARDB_USER = os.getenv('CLEARDB_USER')
CLEARDB_PASSWORD = os.getenv('CLEARDB_PASSWORD')
if os.getenv('ClearDB env', 'FALSE') == 'TRUE':
    print('Database Running in ClearDB...')
    DB_HOST = 'db'
    DB_USER = CLEARDB_USER,
    DB_PASSWORD = CLEARDB_PASSWORD, 
    DB_DATABASE = 'mywebdb'
else:
    print('Database Running in Local Env....')
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWORD = 'password'
    DB_DATABASE = 'mywebdb'

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
########## Database Init End ##########


########## Auth Init Start ##########
# Init Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Get admin login info
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD') # Get passwords from .env file
admin_password_hashed = bcrypt.hashpw(ADMIN_PASSWORD.encode('utf-8'), bcrypt.gensalt()) # Hash the passwords using bcrypt
users_db = {
    0: ['admin-baosen', admin_password_hashed]
}

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, db_user_id, username):
        self.id = db_user_id
        self.username = username

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    user_info = users_db.get(int(user_id))
    if user_info:
        return User(user_id, user_info[0])
    return None
########## Auth Init End ##########


########## Routes Start ##########
# Route for the all projects display page
@app.route('/')
def all_projects():
    connection, cursor = get_db_connection()
    cursor.execute('SELECT * FROM projectsTable ORDER BY start_date DESC')
    projects_to_html = cursor.fetchall()

    # Encode image data to Base64
    for one_project_to_html in projects_to_html:
        if one_project_to_html['image']:
            one_project_to_html['image'] = base64.b64encode(one_project_to_html['image']).decode('utf-8')

        one_project_to_html['start_date'] = one_project_to_html['start_date'].strftime('%Y/%m/%d')
        if one_project_to_html['end_date']:
            one_project_to_html['end_date'] = one_project_to_html['end_date'].strftime('%Y/%m/%d')

    connection.close()
    return render_template('all_projects.html', projects_in_html=projects_to_html)

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_form = request.form['username']
        password_form = request.form['password'].encode('utf-8')

        for user_id, user_info in users_db.items():
            if username_form == user_info[0] and bcrypt.checkpw(password_form, user_info[1]):
                user = User(user_id, user_info[0])
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('all_projects'))
        
        flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

# Route to create a new project
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_project():
    if request.method == 'POST':
        title = request.form['title']
        label = request.form['label']
        start_date = request.form['start_date']
        end_date = request.form.get('end_date')
        is_present = request.form.get('is_present') == 'on'
        content = request.form['content']
        image = request.files['image']

        if image:
            image_data = image.read()
        else:
            image_data = None
        
        if is_present:
            end_date = None

        connection, cursor = get_db_connection()
        cursor.execute('INSERT INTO projectsTable ' +
                       '(title, label, start_date, end_date, is_present, content, image) ' +
                       'VALUES (%s, %s, %s, %s, %s, %s, %s)', (title, label, start_date, end_date, is_present, content, image_data))
        connection.commit()
        connection.close()
        
        flash('Project created successfully!', 'success')
        return redirect(url_for('all_projects'))
    
    return render_template('create_project.html')

# Route to read a single project
@app.route('/project/<int:id>')
def read_project(id):
    connection, cursor = get_db_connection()
    cursor.execute('SELECT * FROM projectsTable WHERE id = %s', (id,))
    project_to_html = cursor.fetchone()
    
    # Encode image data to Base64
    if project_to_html['image']:
        project_to_html['image'] = base64.b64encode(project_to_html['image']).decode('utf-8')

    connection.close()
    return render_template('read_project.html', project_in_html=project_to_html)

# Route to update an existing project
@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_project(id):
    connection, cursor = get_db_connection()
    cursor.execute('SELECT * FROM projectsTable WHERE id = %s', (id,))
    project_to_html = cursor.fetchone()

    # Encode image data to Base64
    if project_to_html['image']:
        project_to_html['image'] = base64.b64encode(project_to_html['image']).decode('utf-8')

    connection.close()

    if request.method == 'POST':
        title = request.form['title']
        label = request.form['label']
        start_date = request.form['start_date']
        end_date = request.form.get('end_date')
        is_present = request.form.get('is_present') == 'on'
        content = request.form['content']
        image = request.files['image']
        
        if image:
            image_data = image.read()
        else:
            image_data = None
        
        if is_present:
            end_date = None

        connection, cursor = get_db_connection()
        cursor.execute('UPDATE projectsTable SET title = %s, label = %s, start_date = %s, '+
                       'end_date = %s, is_present = %s, content = %s, image = %s ' + 
                       'WHERE id = %s', (title, label, start_date, end_date, is_present, content, image_data, id))
        connection.commit()
        connection.close()
        
        flash('Project updated successfully!', 'success')
        return redirect(url_for('all_projects'))
    
    return render_template('update_project.html', post_in_html=project_to_html)

# Route to delete a project
@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_project(id):
    connection, cursor = get_db_connection()
    cursor.execute('DELETE FROM projectsTable WHERE id = %s', (id,))
    connection.commit()
    connection.close()
    
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('all_projects'))

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('all_projects'))
########## Routes End ##########

if __name__ == '__main__':
    app.run(debug=True)
