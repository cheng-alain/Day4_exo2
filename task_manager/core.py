import json
import os
from task_manager.logger import setup_logger

TASKS_FILE = os.getenv("TASKS_FILE_PATH", "tasks.json")
logger = setup_logger()

def load_tasks():
    """Load tasks from the tasks file"""
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        else:
            logger.info(f"Tasks file {TASKS_FILE} not found. Creating new.")
            return []
    except Exception as e:
        logger.error(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """Save tasks to the tasks file"""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
        logger.info(f"Tasks saved to {TASKS_FILE}")
        return True
    except Exception as e:
        logger.error(f"Error saving tasks: {e}")
        return False

def add_task(description, priority):
    """Add a new task"""
    tasks = load_tasks()
    
    # Generate a new ID (max existing ID + 1, or 1 if no tasks)
    new_id = 1
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    
    # Create new task
    new_task = {
        "id": new_id,
        "description": description,
        "priority": priority
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    logger.info(f"Task added: ID={new_id}, Description={description}, Priority={priority}")
    return new_task

def list_tasks():
    """List all tasks"""
    tasks = load_tasks()
    logger.info(f"Retrieved {len(tasks)} tasks")
    return tasks

def delete_task(task_id):
    """Delete a task by ID"""
    tasks = load_tasks()
    initial_count = len(tasks)
    
    # Filter out the task with the given ID
    tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(tasks) == initial_count:
        logger.warning(f"Task {task_id} not found")
        return False
    
    save_tasks(tasks)
    logger.info(f"Task {task_id} deleted")
    return True