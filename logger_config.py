import logging

# configure logging
logging.basicConfig(
    filename = 'pipeline.log',
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s- %(message)s"
    
    
)

# create a logger object you can reuse

logger = logging.getLogger("daily_sales_logger")