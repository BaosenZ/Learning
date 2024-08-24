from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',  # Replace with your MySQL host
        user='root',       # Replace with your MySQL user
        password='password',  # Replace with your MySQL password
        database='linkedin_demo'
    )

# Route to display the form and saved experiences
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Modify the SQL query to order by start_date
    cursor.execute("SELECT * FROM experiences ORDER BY start_date ASC")
    experiences = cursor.fetchall()

    cursor.close()
    connection.close()

    # Format the dates for display in "year/month/day" format
    for experience in experiences:
        experience['start_date'] = experience['start_date'].strftime('%Y/%m/%d')
        if experience['end_date']:
            experience['end_date'] = experience['end_date'].strftime('%Y/%m/%d')

    return render_template('index.html', experiences=experiences)

# Route to handle form submission
@app.route('/add_experience', methods=['POST'])
def add_experience():
    start_date = request.form['start_date']
    end_date = request.form.get('end_date')
    is_present = request.form.get('is_present') == 'on'

    connection = get_db_connection()
    cursor = connection.cursor()

    if is_present:
        end_date = None

    cursor.execute(
        "INSERT INTO experiences (start_date, end_date, is_present) VALUES (%s, %s, %s)",
        (start_date, end_date, is_present)
    )

    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
