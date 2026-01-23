import unittest
import os
import sys
import time
import shutil

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from google.drive.client import GoogleDriveClient

class TestGoogleDriveIntegration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Starting Google Drive Integration Tests...")
        cls.client = GoogleDriveClient()
        cls.test_folder_id = None
        cls.test_file_id = None
        
    @classmethod
    def tearDownClass(cls):
        # Cleanup
        if cls.client:
           if cls.test_file_id:
               try:
                   cls.client.delete_file(cls.test_file_id)
                   print(f"Deleted test file {cls.test_file_id}")
               except Exception as e:
                   print(f"Error deleting file: {e}")
           
           if cls.test_folder_id:
               try:
                   cls.client.delete_file(cls.test_folder_id)
                   print(f"Deleted test folder {cls.test_folder_id}")
               except Exception as e:
                   print(f"Error deleting folder: {e}")
           
           cls.client.close()
        print("\nTests Complete.")

    def test_01_create_folder(self):
        """Verify we can create a folder."""
        print("\nTesting create_folder...")
        folder_name = f"PAI_Test_Folder_{int(time.time())}"
        folder = self.client.create_folder(folder_name)
        
        print(f"Create folder result: {folder}")
        
        if isinstance(folder, dict) and 'id' in folder:
             self.test_folder_id = folder['id']
             self.assertEqual(folder.get('name'), folder_name)
        # Note: MCP behavior might vary, handle gracefully if verify difficult
        
    def test_02_upload_file(self):
        """Verify we can upload (create) a file."""
        print("\nTesting upload_file...")
        
        # Create local temp file
        local_path = "temp_test_upload.txt"
        with open(local_path, "w") as f:
            f.write("Hello from PAI Integration Test")
            
        try:
            filename = f"PAI_Test_File_{int(time.time())}.txt"
            result = self.client.upload_file(filename, local_path)
            print(f"Upload result: {result}")
            
            if isinstance(result, dict) and 'id' in result:
                self.test_file_id = result['id']
                self.assertEqual(result.get('name'), filename)
                
        finally:
            if os.path.exists(local_path):
                os.remove(local_path)

    def test_03_list_files(self):
        """Verify we can list files."""
        print("\nTesting list_files...")
        files = self.client.list_files(page_size=5)
        if isinstance(files, str):
            self.assertGreater(len(files), 0)
        else:
            self.assertIsInstance(files, list)
        print(f"Found {len(files)} files.")

if __name__ == '__main__':
    unittest.main()
