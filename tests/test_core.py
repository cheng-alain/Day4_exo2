import unittest
import os
import json
import tempfile
from task_manager.core import add_task, load_tasks, delete_task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Set up temporary task file for testing"""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_filename = self.temp_file.name
        self.temp_file.close()
        
        # Set the environment variable to point to our test file
        os.environ["TASKS_FILE_PATH"] = self.temp_filename
        
        # Import the module again to pick up the new environment variable
        import task_manager.core
        # Update the TASKS_FILE variable directly
        task_manager.core.TASKS_FILE = self.temp_filename

    def tearDown(self):
        """Clean up the temporary file"""
        os.unlink(self.temp_filename)
        
    def test_add_task(self):
        """Test adding a task"""
        # Add a task
        task = add_task("Test task", 1)
        
        # Verify the task was added
        self.assertEqual(task["description"], "Test task")
        self.assertEqual(task["priority"], 1)
        self.assertEqual(task["id"], 1)
        
        # Verify the task was saved to the file
        with open(self.temp_filename, 'r') as f:
            tasks = json.load(f)
            
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task")
        
    def test_delete_task(self):
        """Test deleting a task"""
        # Add two tasks
        add_task("Task 1", 1)
        add_task("Task 2", 2)
        
        # Verify they were added
        tasks = load_tasks()
        self.assertEqual(len(tasks), 2)
        
        # Delete the first task
        result = delete_task(1)
        self.assertTrue(result)
        
        # Verify it was deleted
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Task 2")
        
        # Try to delete a non-existent task
        result = delete_task(99)
        self.assertFalse(result)
        
        # Verify no changes were made
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)

if __name__ == "__main__":
    unittest.main()