#Fetch data from MongoDB. Insert into MYSQL database.
import mysql.connector
from pymongo import MongoClient
from config import MONGO_URI, MYSQL_CONFIG
from utils import log

def load_to_mysql():
    log("Fetching data from MongoDB and loading into MySQL...")

    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client["server_logs"]
    collection = db["user_history"]

    # Fetch data from MongoDB
    data = list(collection.find({}, {"_id": 0, "email": 1, "date": 1}))

    if not data:
        log("No data found in MongoDB. Skipping MySQL insertion.")
        return  # Exit if no data

    # Connect to MySQL
    mysql_connection = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = mysql_connection.cursor()

    # ✅ Fixed: Corrected SQL syntax
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            date DATETIME NOT NULL
        );
    """)

    # Insert records
    insert_query = "INSERT INTO user_history (email, date) VALUES (%s, %s)"
    cursor.executemany(insert_query, [(d["email"], d["date"]) for d in data])

    # Commit and close
    mysql_connection.commit()
    cursor.close()
    mysql_connection.close()

    log("Data successfully loaded into MySQL.")
