# 📊 Server Log Data Extraction and User History Database Update, By GUVI.

## 📖 Project Overview 
The "Server Log Data Extraction and User History Database Update" project automates the extraction of email addresses and timestamps from server log files. Using Python and Regex, the extracted data is stored in MongoDB and later transferred to MySQL for structured analysis. The system helps track user activity trends, providing insights such as unique email addresses, email frequency per day, and domain-based email distribution.

## 🚀 Objectives  
- Extract email and timestamps from raw server logs.
- Store extracted data in MongoDB for flexible querying.
- Transfer data to MySQL for structured analysis.
- Provide insights into user activity trends.

## 🛠️ Tools & Technologies  
- **Python**: ETL scripting, data processing  
- **Regex**: Extracting email addresses & timestamps  
- **MongoDB**: Storing unstructured extracted data  
- **MySQL / SQLite**: Structured database for querying  
- **pymongo, mysql-connector-python**: Database connectivity  

## 🏗️ ETL Process  
1️⃣ **Extract**: Read raw server logs, apply Regex to extract email and timestamps  
2️⃣ **Transform**: Convert timestamps to a structured `datetime` format  
3️⃣ **Load**: Store structured data into MongoDB and then MySQL for analysis  

## 📊 Data Insights  
- Number of unique email addresses  
- Emails count per day(Number of emails sent per day)  
- First and last email record activity per user  
- Domain-wise email distribution

**Conclusion & Future Enhancements**  
   ✅ Successfully automated log data extraction  
   ✅ Improved structured storage for efficient querying  
   🚀 **Future Scope:** Add real-time log processing, integrate with cloud databases  

## 🔧 How to Run  
```bash
# Clone the repository
git clone https://github.com/your_username/server-log-etl.git

# Install dependencies
pip install -r requirements.txt

# Run the ETL pipeline
python etl_pipeline.py
