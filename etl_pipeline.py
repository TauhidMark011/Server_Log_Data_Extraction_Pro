from extraction import extract_email_and_dates
from transformation import transform_data
from mongodb_loader import save_to_mongodb
from mysql_loader import load_to_mysql
from queries import run_queries
from config import RAW_FILE_PATH
from utils import log

if __name__ == "__main__":
    log("ETL_Process started...")
    #Extract..
    extracted_data = extract_email_and_dates(RAW_FILE_PATH)
    #Transform..
    transformed_data = transform_data(extracted_data)
    #Load to MongoDB
    save_to_mongodb(transformed_data)
    #Load to MYSQL
    load_to_mysql()
    #Run Queries 
    run_queries()

