import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='loki.log',     
    filemode='w'             
)

# Create logger
logger = logging.getLogger()

# Log messages
logger.debug("This is a debug message")
logger.info("Program started")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print("Check loki.log file for logs.")