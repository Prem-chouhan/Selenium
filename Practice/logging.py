import logging

logging.basicConfig(filename="/home/admin-1/prem/test.log")

logger = logging.getLogger()

logger.debug("this is debug message")
logger.info("this is info message")
logger.warning("this is warning message")
logger.error("this is error message")
logger.critical("this is critical message")

