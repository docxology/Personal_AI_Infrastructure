from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleClassroomClient(UniversalGoogleClient):
    """
    Client for the Google Classroom API (classroom v1).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='classroom', version='v1')

    def list_courses(self, page_size: int = 100) -> List[Dict[str, Any]]:
        """List all courses the user has access to."""
        if not self.is_ready():
            return []
        result = self.service.courses().list(pageSize=page_size).execute()
        return result.get('courses', [])

    def get_course(self, course_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific course by ID."""
        if not self.is_ready():
            return None
        return self.service.courses().get(id=course_id).execute()

    def list_students(self, course_id: str) -> List[Dict[str, Any]]:
        """List students in a course."""
        if not self.is_ready():
            return []
        result = self.service.courses().students().list(courseId=course_id).execute()
        return result.get('students', [])
