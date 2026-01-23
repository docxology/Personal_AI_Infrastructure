from typing import Dict, Any, List, Optional
import os
import logging
from google.base_client import GoogleMCPClient
from google.utils import get_base_credentials_path, load_google_credentials_env

class GoogleTasksClient(GoogleMCPClient):
    """
    A Python client that interfaces with the Google Tasks MCP tools (via @dav23/google-mcp).
    Enhanced with comprehensive task and tasklist management methods.
    """
    
    def __init__(self, 
                 credentials_path: Optional[str] = None):
        
        self.credentials_path = credentials_path or get_base_credentials_path()
        
        env = os.environ.copy()
        try:
            env.update(load_google_credentials_env())
        except Exception as e:
            logging.warning(f"Failed to load credentials for env: {e}")
        
        super().__init__(
            server_command=["npx", "-y", "@dav23/google-mcp", "start"],
            env=env
        )

    # =====================
    # Task List Operations
    # =====================

    def list_tasklists(self) -> List[Dict[str, Any]]:
        """List all task lists."""
        return self.call_tool("google_tasks_list_tasklists", {})

    def create_tasklist(self, title: str) -> Dict[str, Any]:
        """Create a new task list."""
        return self.call_tool("google_tasks_create_tasklist", {"title": title})

    def delete_tasklist(self, tasklist_id: str) -> Dict[str, Any]:
        """Delete a task list."""
        return self.call_tool("google_tasks_delete_tasklist", {"taskListId": tasklist_id})

    def set_default_tasklist(self, tasklist_id: str) -> Dict[str, Any]:
        """Set the default task list ID."""
        return self.call_tool("google_tasks_set_default_list", {"taskListId": tasklist_id})

    # =====================
    # Task Operations
    # =====================

    def list_tasks(self, tasklist_id: str, show_completed: bool = True,
                   show_hidden: bool = False) -> List[Dict[str, Any]]:
        """
        List tasks in a specific list.
        
        Args:
            tasklist_id: The task list ID
            show_completed: Include completed tasks
            show_hidden: Include hidden/deleted tasks
        """
        args = {"taskListId": tasklist_id}
        if not show_completed:
            args["showCompleted"] = False
        if show_hidden:
            args["showHidden"] = True
        return self.call_tool("google_tasks_list_tasks", args)

    def get_task(self, task_id: str, tasklist_id: Optional[str] = None) -> Dict[str, Any]:
        """Get details about a specific task."""
        args = {"taskId": task_id}
        if tasklist_id: 
            args["taskListId"] = tasklist_id
        return self.call_tool("google_tasks_get_task", args)

    def create_task(self, tasklist_id: str, title: str, notes: str = "",
                    due: Optional[str] = None, parent: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new task.
        
        Args:
            tasklist_id: The task list ID
            title: Task title
            notes: Task description/notes
            due: Due date in RFC 3339 format (e.g., '2024-12-31T00:00:00.000Z')
            parent: Parent task ID for creating subtasks
        """
        args = {
            "taskListId": tasklist_id,
            "title": title,
            "notes": notes
        }
        if due:
            args["due"] = due
        if parent:
            args["parent"] = parent
        return self.call_tool("google_tasks_create_task", args)

    def update_task(self, task_id: str, tasklist_id: Optional[str] = None, 
                   title: Optional[str] = None, notes: Optional[str] = None, 
                   due: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
        """
        Update an existing task.
        
        Args:
            task_id: The task ID
            tasklist_id: The task list ID (uses default if not specified)
            title: New title
            notes: New notes
            due: New due date
            status: New status ('needsAction' or 'completed')
        """
        args = {"taskId": task_id}
        if tasklist_id: 
            args["taskListId"] = tasklist_id
        if title: 
            args["title"] = title
        if notes: 
            args["notes"] = notes
        if due: 
            args["due"] = due
        if status: 
            args["status"] = status
        return self.call_tool("google_tasks_update_task", args)

    def complete_task(self, task_id: str, tasklist_id: Optional[str] = None) -> Dict[str, Any]:
        """Mark a task as completed."""
        args = {"taskId": task_id}
        if tasklist_id: 
            args["taskListId"] = tasklist_id
        return self.call_tool("google_tasks_complete_task", args)

    def delete_task(self, tasklist_id: str, task_id: str) -> Dict[str, Any]:
        """Delete a task."""
        return self.call_tool("google_tasks_delete_task", {
            "taskListId": tasklist_id,
            "taskId": task_id
        })

    # =====================
    # Advanced Operations
    # =====================

    def move_task(self, task_id: str, tasklist_id: str, 
                  parent: Optional[str] = None, 
                  previous: Optional[str] = None) -> Dict[str, Any]:
        """
        Move a task to a new position or make it a subtask.
        
        Args:
            task_id: The task to move
            tasklist_id: The task list ID
            parent: ID of parent task (to make this a subtask)
            previous: ID of task to insert after (for ordering)
        """
        args = {
            "taskId": task_id,
            "taskListId": tasklist_id
        }
        if parent:
            args["parent"] = parent
        if previous:
            args["previous"] = previous
        return self.call_tool("google_tasks_move_task", args)

    def clear_completed(self, tasklist_id: str) -> Dict[str, Any]:
        """Remove all completed tasks from a task list."""
        return self.call_tool("google_tasks_clear_completed", {"taskListId": tasklist_id})

    def batch_create_tasks(self, tasklist_id: str, 
                           tasks: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """
        Create multiple tasks at once.
        
        Args:
            tasklist_id: The task list ID
            tasks: List of task dicts with 'title' and optional 'notes', 'due' keys
        
        Returns:
            List of created task responses
        """
        results = []
        for task in tasks:
            result = self.create_task(
                tasklist_id=tasklist_id,
                title=task.get('title', 'Untitled'),
                notes=task.get('notes', ''),
                due=task.get('due')
            )
            results.append(result)
        return results

    def get_all_tasks(self, tasklist_id: str, show_completed: bool = True) -> List[Dict[str, Any]]:
        """
        Get all tasks with automatic pagination handling.
        
        Note: The MCP tool may have pagination limits. This attempts to retrieve
        all available tasks in a single call.
        """
        return self.list_tasks(tasklist_id, show_completed=show_completed)

    def get_pending_tasks(self, tasklist_id: str) -> List[Dict[str, Any]]:
        """Get only incomplete/pending tasks."""
        return self.list_tasks(tasklist_id, show_completed=False)

    def get_overdue_tasks(self, tasklist_id: str) -> List[Dict[str, Any]]:
        """
        Get tasks that are past due.
        
        Returns tasks where 'due' date is before today and status is 'needsAction'.
        """
        from datetime import datetime
        tasks = self.list_tasks(tasklist_id, show_completed=False)
        if not isinstance(tasks, list):
            return []
        
        now = datetime.utcnow().isoformat() + 'Z'
        overdue = []
        for task in tasks:
            due = task.get('due')
            if due and due < now and task.get('status') == 'needsAction':
                overdue.append(task)
        return overdue
