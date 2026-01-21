from typing import Dict, Any, List, Optional
import os
from google.base_client import GoogleMCPClient
from google.utils import get_base_credentials_path, load_google_credentials_env

class GoogleTasksClient(GoogleMCPClient):
    """
    A Python client that interfaces with the Google Tasks MCP tools (via @dav23/google-mcp).
    """
    
    def __init__(self, 
                 credentials_path: Optional[str] = None):
        
        self.credentials_path = credentials_path or get_base_credentials_path()
        
        env = os.environ.copy()
        try:
             env.update(load_google_credentials_env())
        except Exception as e:
             print(f"Warning: Failed to load credentials for env: {e}")
        
        super().__init__(
            server_command=["npx", "-y", "@dav23/google-mcp", "start"],
            env=env
        )

    def list_tasklists(self) -> List[Dict[str, Any]]:
        """List all task lists."""
        return self.call_tool("google_tasks_list_tasklists", {})

    def list_tasks(self, tasklist_id: str) -> List[Dict[str, Any]]:
        """List tasks in a specific list."""
        return self.call_tool("google_tasks_list_tasks", {"taskListId": tasklist_id})

    def create_task(self, tasklist_id: str, title: str, notes: str = "") -> Dict[str, Any]:
        """Create a new task."""
        return self.call_tool("google_tasks_create_task", {
            "taskListId": tasklist_id,
            "title": title,
            "notes": notes
        })

    def delete_task(self, tasklist_id: str, task_id: str):
        """Delete a task."""
        return self.call_tool("google_tasks_delete_task", {
            "taskListId": tasklist_id,
            "taskId": task_id
        })

    def set_default_tasklist(self, tasklist_id: str) -> Dict[str, Any]:
        """Set the default task list ID."""
        return self.call_tool("google_tasks_set_default_list", {"taskListId": tasklist_id})

    def get_task(self, task_id: str, tasklist_id: Optional[str] = None) -> Dict[str, Any]:
        """Get details about a specific task."""
        args = {"taskId": task_id}
        if tasklist_id: args["taskListId"] = tasklist_id
        return self.call_tool("google_tasks_get_task", args)

    def update_task(self, task_id: str, tasklist_id: Optional[str] = None, 
                   title: Optional[str] = None, notes: Optional[str] = None, 
                   due: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
        """Update an existing task."""
        args = {"taskId": task_id}
        if tasklist_id: args["taskListId"] = tasklist_id
        if title: args["title"] = title
        if notes: args["notes"] = notes
        if due: args["due"] = due
        if status: args["status"] = status
        return self.call_tool("google_tasks_update_task", args)

    def complete_task(self, task_id: str, tasklist_id: Optional[str] = None) -> Dict[str, Any]:
        """Mark a task as completed."""
        args = {"taskId": task_id}
        if tasklist_id: args["taskListId"] = tasklist_id
        return self.call_tool("google_tasks_complete_task", args)

    def create_tasklist(self, title: str) -> Dict[str, Any]:
        """Create a new task list."""
        return self.call_tool("google_tasks_create_tasklist", {"title": title})

    def delete_tasklist(self, tasklist_id: str) -> Dict[str, Any]:
        """Delete a task list."""
        return self.call_tool("google_tasks_delete_tasklist", {"taskListId": tasklist_id})
