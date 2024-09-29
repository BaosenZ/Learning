from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)


# MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Replace with your MySQL host
        user="root",  # Replace with your MySQL user
        password="password",  # Replace with your MySQL password
        database="blogs_sort_demo",
    )


# Route to display the form and saved experiences
@app.route("/")
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM blogs ORDER BY sort_order ASC")
    blogs = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", blogs=blogs)


# Route to update sort order
@app.route("/update_order", methods=["POST"])
def update_order():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()

    for sort_order, blog_id in enumerate(data["order"]):
        cursor.execute(
            "UPDATE blogs SET sort_order = %s WHERE id = %s", (sort_order, blog_id)
        )

    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)
