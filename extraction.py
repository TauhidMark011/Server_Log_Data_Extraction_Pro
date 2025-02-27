import re
from utils import log
def extract_email_and_dates(file_path):
    log(f"Extracting email address and dates from{file_path}")
    email_pattern = re.compile(r"From: (\S+@\S+)")
    date_pattern = re.compile(r"^Date: (.*)$")
    extracted_data = []
    with open(file_path, "r", encoding="UTF 8") as file:
        lines = file.readlines()
        current_email = None
        current_date = None
        for line in lines:
            email_match = email_pattern.search(line)
            date_match = date_pattern.search(line)
            if email_match:
                current_email = email_match.group(1)
            if date_match: 
                current_date = date_match.group(1)
            if current_email and current_date:
                extracted_data.append((current_email, current_date))
                current_email, current_date = None, None
    log(f"Extracted {len(extracted_data)} email-date pairs.")
    return extracted_data



    