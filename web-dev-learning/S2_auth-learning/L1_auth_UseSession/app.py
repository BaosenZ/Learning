from flask import Flask, render_template, redirect, request, url_for, session, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_secret_key'

# users minic database, using python dictionary
users_minic_db = {
    0: ['admin', 'mypassword'],
    1: ['user1', 'user1password']
}

# Route for the home page
@app.route('/')
def home():
    # myNote: In the `index.html``, we only check session["currentUser"] exists. 
    # To make auth better, we might pass the usernames in `users_minic_bd` to the `index.html`. 
    # Same for blog page. 
    return render_template('index.html')  
    
# Route for the blog page
@app.route('/blog')
def blog():
    # Same with home page
    return render_template('blog.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_form = request.form['username']
        password_form = request.form['password']

        # Loop over the users in the mini-database for authentication check
        for user_id, user_info in users_minic_db.items():
            if username_form == user_info[0] and password_form == user_info[1]:
                session['currentUser'] = user_info[0]  # myNote: Only store the username into the session. The session name is `currentUser` for both users
                flash('Login successful!', 'success')
                return redirect(url_for('home'))
        
        flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

# Route for editing the blog (only accessible when logged in)
@app.route('/edit', methods=['GET', 'POST'])
def edit_blog():
    if 'currentUser' not in session:
        flash('You need to log in to edit the blog.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        flash('Blog updated! (I dont implement it~)', 'success')
        return redirect(url_for('blog'))

    return render_template('edit.html')

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('currentUser', None)
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
