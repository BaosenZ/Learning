from flask import Flask, jsonify, render_template, request
import json

# import mysql.connector

app = Flask(__name__)
app.config["SECRET_KEY"] = "flask_secret_key"

# # MySQL database configuration
# if os.getenv('ClearDB env', 'FALSE') == 'TRUE':
#     print('Database Running in clearDB...')
#     DB_HOST = 'db'
#     DB_USER = 'dbmaster'
#     DB_PASSWORD = ''
#     DB_DATABASE = 'blogdb'
# else:
#     print('Database Running in local env....')
#     DB_HOST = '127.0.0.1'
#     DB_USER = 'root'
#     DB_PASSWORD = 'password'  # update to your MySQL database password
#     DB_DATABASE = 'blogdb'

# # Function to get database connection
# def get_db_connection():
#     connection = mysql.connector.connect(
#         host=DB_HOST,
#         user=DB_USER,
#         password=DB_PASSWORD,
#         database=DB_DATABASE
#     )
#     cursor = connection.cursor(dictionary=True)
#     return connection, cursor


# Load the mock database from the JSON file
def load_data():
    with open("data.json") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data", methods=["GET"])
def get_data():
    # Get pagination parameters from request
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

    # Load all data
    data = load_data()

    # Implement server-side pagination
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = data[start:end]

    total_count = len(data)

    response = {
        "data": paginated_data,
        "page": page,
        "per_page": per_page,
        "total_count": total_count,
        "total_pages": (total_count + per_page - 1) // per_page,  # Ceiling division
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
