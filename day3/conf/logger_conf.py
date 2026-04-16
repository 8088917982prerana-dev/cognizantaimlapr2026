#configure logging
import logging
"""
setup logger for healthcare application
"""
def setup_logger():
    """
    Set up a logger for the healthcare application.
    """
    logger = logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)
    """
    Check if the logger already has handlers to avoid adding multiple handlers
    """
    if logger.hasHandlers():
        return logger
    """
    create file handler to write logs to a file
    """
    file_handler = logging.FileHandler('healthcare.log')
    logger.setLevel(logging.DEBUG)
    """
    Create formatters and add to handlers
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger