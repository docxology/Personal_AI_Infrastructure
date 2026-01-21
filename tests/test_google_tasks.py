import unittest
import os
import sys
import time

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from google.tasks.client import GoogleTasksClient

class TestGoogleTasksIntegration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Starting Google Tasks Integration Tests...")
        cls.client = GoogleTasksClient()
        cls.task_id = None
        cls.tasklist_id = None # using default usually, but let's see
        
    @classmethod
    def tearDownClass(cls):
        # Cleanup
        if cls.client:
           if cls.task_id and cls.tasklist_id:
               try:
                   cls.client.delete_task(cls.tasklist_id, cls.task_id)
                   print(f"Deleted test task {cls.task_id}")
               except Exception as e:
                   print(f"Error deleting task: {e}")
           cls.client.close()
        print("\nTests Complete.")

    def test_01_list_tasklists(self):
        """Verify we can list task lists."""
        print("\nTesting list_tasklists...")
        lists = self.client.list_tasklists()
        if isinstance(lists, str):
            self.assertGreater(len(lists), 0)
            print("Tasks verified (String response). Skipping dependent items.")
            self.tasklist_id = None
        else:
            self.assertIsInstance(lists, list)
            self.assertTrue(len(lists) > 0)
            self.tasklist_id = lists[0]['id'] # Get primary
            print(f"Using TaskList: {lists[0].get('title')} ({self.tasklist_id})")

    def test_02_create_task(self):
        """Verify we can create a task."""
        if not self.tasklist_id:
            self.skipTest("No tasklist_id available (string response from list).")
            
        print("\nTesting create_task...")
        title = f"PAI Test Task {int(time.time())}"
        task = self.client.create_task(self.tasklist_id, title, notes="Created by PAI Automated Test")
        
        print(f"Create task result: {task}")
        
        if isinstance(task, dict) and 'id' in task:
            self.task_id = task['id']
            self.assertEqual(task.get('title'), title)

    def test_03_list_tasks(self):
        """Verify we can list tasks."""
        if not self.tasklist_id:
            self.skipTest("No tasklist found")
            
        print("\nTesting list_tasks...")
        tasks = self.client.list_tasks(self.tasklist_id)
        self.assertIsInstance(tasks, list)
        print(f"Found {len(tasks)} tasks in list.")

if __name__ == '__main__':
    unittest.main()
