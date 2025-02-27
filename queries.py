import mysql.connector
from config import MYSQL_CONFIG
def run_queries():
    #connect to MYSQL
    mysql_conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = mysql_conn.cursor()
    queries = {
        "List all unique email address": "SELECT DISTINCT email FROM user_history;",
        "Count emails per day": "SELECT DATE(date) AS day, COUNT(email) FROM user_history GROUP BY day;",
        #The query finds the first and last email date for each email address from the user_history table.
        "First and last email date per email": """
         SELECT email, MIN(date) as first_email, MAX(date) as last_email
         FROM user_history GROUP BY email;
        """,
        "Count emails per domain" : """
         SELECT SUBSTRING_INDEX(email, '@', -1) AS domain, COUNT(email)
         FROM user_history GROUP BY domain; 
        """
    }

    for title, query in queries.items():
        print(f"\n{title}:")
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    #close connection 
    cursor.close()
    mysql_conn.close()
#Run the query when the script is executed
if __name__ == "__main__":
    run_queries
