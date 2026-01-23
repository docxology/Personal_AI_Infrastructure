from typing import Dict, Any, List, Optional
import os
import logging
from google.base_client import GoogleMCPClient
from google.utils import get_base_credentials_path, get_base_token_path

class GoogleCalendarClient(GoogleMCPClient):
    """
    A Python client that interfaces with the Google Calendar MCP server.
    """
    
    def __init__(self, 
                 credentials_path: Optional[str] = None, 
                 token_path: Optional[str] = None):
        
        self.credentials_path = credentials_path or get_base_credentials_path()
        self.token_path = token_path or get_base_token_path()
        
        env = os.environ.copy()
        env["GOOGLE_OAUTH_CREDENTIALS"] = self.credentials_path
        env["GOOGLE_CALENDAR_MCP_TOKEN_PATH"] = self.token_path
        
        super().__init__(
            server_command=["npx", "-y", "@cocal/google-calendar-mcp", "start"],
            env=env
        )

    def list_calendars(self) -> List[Dict[str, Any]]:
        """List available calendars."""
        res = self.call_tool("list-calendars", {})
        if isinstance(res, dict) and "calendars" in res:
            return res["calendars"]
        return res

    def list_events(self, calendar_id: str = "primary", max_results: int = 10, 
                   time_min: Optional[str] = None, time_max: Optional[str] = None) -> List[Dict[str, Any]]:
        """List events from a calendar."""
        args = {
            "calendarId": calendar_id, 
            "maxResults": max_results
        }
        if time_min: args["timeMin"] = time_min
        if time_max: args["timeMax"] = time_max
        res = self.call_tool("list-events", args)
        if isinstance(res, dict) and "events" in res:
            return res["events"]
        return res

    def create_event(self, summary: str, start_time: str, end_time: str, 
                    calendar_id: str = "primary", description: str = "") -> Dict[str, Any]:
        """Create a new event."""
        res = self.call_tool("create-event", {
            "calendarId": calendar_id,
            "summary": summary,
            "start": start_time,
            "end": end_time,
            "description": description
        })
        if isinstance(res, dict) and "event" in res:
            return res["event"]
        return res
    
    def update_event(self, event_id: str, calendar_id: str = "primary", **kwargs) -> Dict[str, Any]:
        """Update an existing event."""
        args = {
            "eventId": event_id, 
            "calendarId": calendar_id
        }
        if "start_time" in kwargs: args["start"] = kwargs.pop("start_time")
        if "end_time" in kwargs: args["end"] = kwargs.pop("end_time")
        args.update(kwargs)
        res = self.call_tool("update-event", args)
        if isinstance(res, dict) and "event" in res:
            return res["event"]
        return res
        
    def delete_event(self, event_id: str, calendar_id: str = "primary"):
        """Delete an event."""
        return self.call_tool("delete-event", {
            "eventId": event_id, 
            "calendarId": calendar_id
        })
