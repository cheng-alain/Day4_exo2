import os
import json

class Config:
    """Configuration management class"""
    def __init__(self):
        self.tasks_file = os.getenv("TASKS_FILE_PATH", "tasks.json")
        self.log_file = os.getenv("LOG_FILE_PATH", "logs/task_manager.log")
        
    def get_tasks_file(self):
        return self.tasks_file
        
    def get_log_file(self):
        return self.log_file