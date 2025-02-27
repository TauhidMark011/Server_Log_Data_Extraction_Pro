from datetime import datetime
from utils import log

def transform_data(extracted_data):
    log("Transforming data format...")
    transformed_data = []

    for email, date_str in extracted_data:
        try:
            # Corrected strptime format
            formatted_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d %H:%M:%S")
            transformed_data.append((email, formatted_date))  # Fixed tuple format
        except ValueError:
            log(f"Skipping invalid date format: {date_str}")
            continue  # Skip invalid records

    log(f"Transformed {len(transformed_data)} records successfully.")  
    return transformed_data

# from datetime import datetime
# from utils import log

# def transform_data(extracted_data):
#     log("Transforming data format...")
#     transformed_data = []
#     for email, date_str in extracted_data:
#         try:
#             formatted_date = datetime.strptime(date_str, "%a, %d, %b, %Y, %H:%M:%S %z").strftime("%Y-%m-%d %H:%M:%S") #string parse time
#             transformed_data.append(email, formatted_date)
#         except ValueError :
#             log(f"Skipping invalid date format: {date_str}")
#     log(f"Transformed {len(transformed_data)} recorded successfully.")  
#     return transformed_data

#             from datetime import datetime
# date_str = "2024-02-12 15:30:45"
# date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

# print(date_obj)
# # Output: 2024-02-12 15:30:45
# print(type(date_obj))
# # Output: <class 'datetime.datetime'>
