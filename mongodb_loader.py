from pymongo import MongoClient
from utils import log

def save_to_mongodb(documents, db_name="server_logs", collection_name="user_history"):
    if not documents:
        log("No documents to insert. Skipping MongoDB insertion.")
        return  # Exit if there's nothing to insert

    # Convert (email, date) tuples into dictionaries
    formatted_documents = [{"email": email, "date": date} for email, date in documents]

    try:
        client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
        db = client[db_name]
        collection = db[collection_name]

        result = collection.insert_many(formatted_documents)
        log(f"Successfully inserted {len(result.inserted_ids)} documents into MongoDB.")

    except Exception as e:
        log(f"Error inserting into MongoDB: {e}")

    finally:
        client.close()  # Ensure connection is closed


# from pymongo import MongoClient
# from config import MONGO_URI
# from utils import log

# def save_to_mongodb(data):
#     log("Saving data to mongoDb...")
#     client = MongoClient(MONGO_URI)
#     db = client["server_logs"]
#     collection = db["user_history"]
#     documents = [{"email": email, "date": date} for email, date in data]
#     collection.insert_many(documents)
#     log("Data successfully stored in MongoDB.")