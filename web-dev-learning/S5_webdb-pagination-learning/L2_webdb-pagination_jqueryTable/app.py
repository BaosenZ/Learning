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


def load_data():
    """Load mock data from JSON file."""
    with open("data.json") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data-source", methods=["POST"])
def data_source():
    # Load all data
    data = load_data()

    # Get parameters from the DataTable request
    draw = int(request.form.get("draw"))
    start = int(request.form.get("start"))
    length = int(request.form.get("length"))
    search_value = request.form.get("search[value]", "")

    # If there's a search term, filter data
    if search_value:
        data = [
            item
            for item in data
            if search_value.lower() in str(item["id"]).lower()
            or search_value.lower() in item["name"].lower()
            or search_value.lower() in str(item["age"]).lower()
            or search_value.lower() in item["email"].lower()
        ]

    # Filter the required data (pagination logic)
    paginated_data = data[start : start + length]

    # Prepare response in DataTables format
    response = {
        "draw": draw,
        "recordsTotal": len(load_data()),  # Total records without filtering
        "recordsFiltered": len(data),  # Total records after filtering
        "data": paginated_data,
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
