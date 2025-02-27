import logging 
logging.basicConfig(
    filename="etlserver_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s"
)

def log(message):
    logging.info(message)
    print(message)