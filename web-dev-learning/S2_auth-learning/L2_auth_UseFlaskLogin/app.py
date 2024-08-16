from flask import Flask, render_template, redirect, session, request, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_secret_key'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, db_user_id, username):
        self.id = db_user_id
        self.username = username

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    for user_id, user_info in users_minic_db.items():
        return User(user_id, user_info)

# users minic database, using python dictionary
users_minic_db = {
    0: ['admin', 'mypassword'],
    1: ['user1', 'user1password']
}

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_form = request.form['username']
        password_form = request.form['password']

        for user_id, user_info in users_minic_db.items():
            if username_form == user_info[0] and password_form == user_info[1]:
                user = User(user_id, user_info[0])
                login_user(user)  # automatically manages the session
                flash('Login successful!', 'success')
                return redirect(url_for('home'))
        
        flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

# Route for editing the blog (only accessible when logged in)
@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_blog():
    if request.method == 'POST':
        flash('Blog updated! (I dont implement it~)', 'success')
        return redirect(url_for('blog'))

    return render_template('edit.html')

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# for session debug
@app.route('/session_check')
def session_check():
    session_data = []
    for key, value in session.items():
        session_data.append(f"{key}: {value}")
    return ", ".join(session_data)

if __name__ == '__main__':
    app.run(debug=True)
