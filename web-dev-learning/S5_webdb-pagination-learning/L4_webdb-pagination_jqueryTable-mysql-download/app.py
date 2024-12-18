from flask import Flask, jsonify, render_template, request, send_file

# import json
import mysql.connector
import csv
import os

# import mysql.connector

app = Flask(__name__)
app.config["SECRET_KEY"] = "flask_secret_key"

# MySQL database configuration
print("Database Running in local env....")
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "password"  # update to your MySQL database password
DB_DATABASE = "blogdb"


# Function to get database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
    )
    cursor = connection.cursor(dictionary=True)
    return connection, cursor


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data-source", methods=["POST"])
def data_source():
    # Get pagination and search parameters from DataTable request
    draw = int(request.form.get("draw"))
    start = int(request.form.get("start"))
    length = int(request.form.get("length"))
    search_value = request.form.get("search[value]", "")

    # Establish database connection
    connection, cursor = get_db_connection()

    # Construct the SQL query with search and limit
    query = "SELECT * FROM users"
    params = []

    # If there's a search term, add a WHERE clause
    if search_value:
        query += " WHERE id LIKE %s OR name LIKE %s OR age LIKE %s OR email LIKE %s"
        search_term = f"%{search_value}%"
        params.extend([search_term] * 4)

    # Get the total number of filtered records (for pagination calculation)
    cursor.execute(query, params)
    filtered_count = len(cursor.fetchall())

    # Add the limit and offset for pagination
    query += " LIMIT %s OFFSET %s"
    params.extend([length, start])

    # Execute the query with pagination
    cursor.execute(query, params)
    records = cursor.fetchall()
    print(records)

    # Get the total number of records without filtering (for pagination calculation)
    cursor.execute("SELECT COUNT(*) AS total FROM users")
    total_count = cursor.fetchone()["total"]

    # Close the database connection
    cursor.close()
    connection.close()

    # Prepare the response in DataTables format
    response = {
        "draw": draw,
        "recordsTotal": total_count,
        "recordsFiltered": filtered_count,
        "data": records,
    }

    return jsonify(response)


@app.route("/download-csv", methods=["GET"])
def download_csv():
    connection, cursor = get_db_connection()

    # Query to select all data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print(rows)
    print(type(rows[0]))

    # Define the CSV file path
    csv_file_path = "all_data.csv"
    with open(csv_file_path, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header
        csvwriter.writerow(rows[0].keys())
        # Write the data rows
        for row in rows:
            csvwriter.writerow(row.values())

    cursor.close()
    connection.close()

    # Send the file to the user for download
    return send_file(csv_file_path, as_attachment=True, download_name="all_data.csv")


if __name__ == "__main__":
    app.run(debug=True)
