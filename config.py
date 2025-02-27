#Keeps credentials & settings separate from the main code.
#Easier to modify configurations without changing multiple files.
#Improves security by avoiding hardcoded credentials in scripts.
# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
# MySQL Configuration (Using MySQL Instead of SQLite)
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1438011",
    "database": "server_logs"
}
#Adding RAW FILE PATH for Log File Processing
RAW_FILE_PATH = "D:/Server_Log_DataExtraction/dataset/mbox.txt"