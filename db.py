import mysql.connector
import json

def create_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="actowiz"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS carwale")
    conn.close()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="actowiz",
        database="carwale"
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS car_details (
        id INT AUTO_INCREMENT PRIMARY KEY,
        brand_name VARCHAR(255),
        brand_url TEXT,
        car_name VARCHAR(255),
        car_url TEXT,
        variant_name VARCHAR(255),
        variant_url TEXT,
        highlights JSON,
        specifications JSON,
        safety JSON,
        features JSON
    )
    """)

    conn.commit()
    conn.close()

def insert_into_db(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO car_details (
        brand_name, brand_url, car_name, car_url,
        variant_name, variant_url,
        highlights, specifications, safety, features
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["brand_name"],
        data["brand_url"],
        data["car_name"],
        data["car_url"],
        data["variant_name"],
        data["variant_url"],
        json.dumps(data["highlights"]),
        json.dumps(data["specifications"]),
        json.dumps(data["safety"]),
        json.dumps(data["features"])
    )

    cursor.execute(query, values)
    conn.commit()
    conn.close()