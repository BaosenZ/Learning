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
    user_to_html = users_minic_db[0][0]
    return render_template('index.html', user_in_html=user_to_html)

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

        # Simple authentication check
        if username_form == users_minic_db[0][0] and password_form == users_minic_db[0][1]:
            session[users_minic_db[0][0]] = users_minic_db[0][0]
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

# Route for editing the blog (only accessible when logged in)
@app.route('/edit', methods=['GET', 'POST'])
def edit_blog():
    if users_minic_db[0][0] not in session:
        flash('You need to log in to edit the blog.', 'danger')
        return redirect('/login')

    if request.method == 'POST':
        flash('Blog updated! (I dont implement it~)', 'success')
        return redirect('/blog')

    if users_minic_db[0][0] in session:
        return render_template('edit.html')
    
# Route for logging out
@app.route('/logout')
def logout():
    session.pop(users_minic_db[0][0], None)
    flash('You have been logged out.', 'info')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
