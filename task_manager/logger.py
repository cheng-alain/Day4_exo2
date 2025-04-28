import logging
import os
from datetime import datetime

def setup_logger(log_file="task_manager.log"):
    """Set up and return a logger object"""
    log_directory = "logs"
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    log_path = os.path.join(log_directory, log_file)
    
    # Create logger
    logger = logging.getLogger("task_manager")
    logger.setLevel(logging.DEBUG)
    
    # Prevent duplicate handlers
    if not logger.handlers:
        # Create file handler
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)
        
        # Create formatter and add it to the handler
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(file_handler)
    
    return logger