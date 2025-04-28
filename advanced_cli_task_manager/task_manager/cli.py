#!/usr/bin/env python3
import argparse
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")
    add_parser.add_argument("--priority", "-p", type=int, choices=[1, 2, 3], default=2,
                          help="Task priority (1=High, 2=Medium, 3=Low)")

    # List Tasks
    list_parser = subparsers.add_parser("list", help="List all tasks")

    # Delete Task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

    # Actions
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.description, args.priority)
        logger.info(f"Task added: {args.description} with priority {args.priority}")
        print(f"Task added: {args.description} with priority {args.priority}")
    
    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for task in tasks:
                print(f"ID: {task['id']} | Description: {task['description']} | Priority: {task['priority']}")
        logger.info("Tasks listed")
    
    elif args.command == "delete":
        success = delete_task(args.task_id)
        if success:
            print(f"Task {args.task_id} deleted.")
            logger.info(f"Task {args.task_id} deleted")
        else:
            print(f"Task {args.task_id} not found.")
            logger.warning(f"Attempted to delete non-existent task {args.task_id}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()