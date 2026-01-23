"""
Coda API Base Client

REST client with Bearer authentication, pagination, and rate limiting.
"""

import json
import time
import logging
from typing import Dict, Any, List, Optional, Iterator
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode

from coda.utils import get_coda_token

logger = logging.getLogger(__name__)


class CodaAPIError(Exception):
    """Exception raised for Coda API errors."""
    
    def __init__(self, message: str, status_code: int = None, response: Dict = None):
        self.status_code = status_code
        self.response = response
        super().__init__(message)


class CodaRateLimitError(CodaAPIError):
    """Exception raised when rate limited (HTTP 429)."""
    pass


class CodaClient:
    """
    Base REST client for Coda.io API v1.5.0.
    
    Features:
    - Bearer token authentication
    - Automatic pagination handling
    - Rate limit detection with retry
    - Request/response logging
    
    Usage:
        client = CodaClient()
        user = client.whoami()
        docs = client.list_docs()
    """
    
    BASE_URL = "https://coda.io/apis/v1"
    
    def __init__(
        self,
        token: Optional[str] = None,
        token_path: Optional[str] = None,
        max_retries: int = 3,
        retry_delay: float = 1.0,
        timeout: int = 60
    ):
        """
        Initialize the Coda API client.
        
        Args:
            token: API token (if not provided, loaded from env/file)
            token_path: Custom path to token.json
            max_retries: Maximum retry attempts for rate limits
            retry_delay: Base delay between retries (exponential backoff)
            timeout: Request timeout in seconds
        """
        self.token = token or get_coda_token(token_path)
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.timeout = timeout
    
    def _get_headers(self) -> Dict[str, str]:
        """Get request headers with authorization."""
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    
    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Make an HTTP request to the Coda API.
        
        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE)
            endpoint: API endpoint (without base URL)
            params: Query parameters
            data: Request body for POST/PUT/PATCH
            
        Returns:
            Parsed JSON response
            
        Raises:
            CodaAPIError: On API errors
            CodaRateLimitError: On rate limiting
        """
        url = f"{self.BASE_URL}{endpoint}"
        
        if params:
            # Filter None values and encode
            filtered = {k: v for k, v in params.items() if v is not None}
            if filtered:
                url = f"{url}?{urlencode(filtered, doseq=True)}"
        
        body = json.dumps(data).encode('utf-8') if data else None
        
        for attempt in range(self.max_retries + 1):
            try:
                request = Request(url, data=body, headers=self._get_headers(), method=method)
                
                logger.debug(f"Coda API {method} {url}")
                
                with urlopen(request, timeout=self.timeout) as response:
                    response_data = response.read().decode('utf-8')
                    if response_data:
                        return json.loads(response_data)
                    return {}
                    
            except HTTPError as e:
                response_body = e.read().decode('utf-8') if e.fp else ""
                
                if e.code == 429:
                    # Rate limited
                    if attempt < self.max_retries:
                        delay = self.retry_delay * (2 ** attempt)
                        logger.warning(f"Rate limited, retrying in {delay}s...")
                        time.sleep(delay)
                        continue
                    raise CodaRateLimitError(
                        f"Rate limited after {self.max_retries} retries",
                        status_code=429
                    )
                
                try:
                    error_data = json.loads(response_body)
                    message = error_data.get("message", str(e))
                except json.JSONDecodeError:
                    message = response_body or str(e)
                
                raise CodaAPIError(message, status_code=e.code, response=error_data if 'error_data' in dir() else None)
                
            except URLError as e:
                raise CodaAPIError(f"Connection error: {e.reason}")
    
    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make a GET request."""
        return self._request("GET", endpoint, params=params)
    
    def _post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make a POST request."""
        return self._request("POST", endpoint, params=params, data=data)
    
    def _put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Make a PUT request."""
        return self._request("PUT", endpoint, data=data)
    
    def _patch(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Make a PATCH request."""
        return self._request("PATCH", endpoint, data=data)
    
    def _delete(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Make a DELETE request."""
        return self._request("DELETE", endpoint, data=data)
    
    def _paginate(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        items_key: str = "items"
    ) -> Iterator[Dict[str, Any]]:
        """
        Iterate through paginated results.
        
        Args:
            endpoint: API endpoint
            params: Initial query parameters
            items_key: Key in response containing items
            
        Yields:
            Individual items from each page
        """
        params = params.copy() if params else {}
        
        while True:
            response = self._get(endpoint, params)
            
            items = response.get(items_key, [])
            for item in items:
                yield item
            
            next_token = response.get("nextPageToken")
            if not next_token:
                break
            
            params["pageToken"] = next_token
    
    def _collect_pages(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        items_key: str = "items",
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Collect all items from paginated endpoint.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            items_key: Key in response containing items
            limit: Maximum items to return (None for all)
            
        Returns:
            List of all items
        """
        items = []
        for item in self._paginate(endpoint, params, items_key):
            items.append(item)
            if limit and len(items) >= limit:
                break
        return items
    
    # -------------------------------------------------------------------------
    # Account / Whoami
    # -------------------------------------------------------------------------
    
    def whoami(self) -> Dict[str, Any]:
        """
        Get info about the current user.
        
        Returns:
            User info including name, loginId, workspace
        """
        return self._get("/whoami")
    
    # -------------------------------------------------------------------------
    # Docs
    # -------------------------------------------------------------------------
    
    def list_docs(
        self,
        is_owner: Optional[bool] = None,
        is_published: Optional[bool] = None,
        is_starred: Optional[bool] = None,
        in_gallery: Optional[bool] = None,
        query: Optional[str] = None,
        source_doc: Optional[str] = None,
        workspace_id: Optional[str] = None,
        folder_id: Optional[str] = None,
        limit: int = 25
    ) -> List[Dict[str, Any]]:
        """
        List available Coda docs.
        
        Args:
            is_owner: Show only owned docs
            is_published: Show only published docs
            is_starred: Show starred/unstarred docs
            in_gallery: Show gallery docs
            query: Search term
            source_doc: Show copies of specific doc
            workspace_id: Filter by workspace
            folder_id: Filter by folder
            limit: Maximum results
            
        Returns:
            List of doc metadata
        """
        params = {
            "isOwner": is_owner,
            "isPublished": is_published,
            "isStarred": is_starred,
            "inGallery": in_gallery,
            "query": query,
            "sourceDoc": source_doc,
            "workspaceId": workspace_id,
            "folderId": folder_id,
            "limit": limit
        }
        return self._collect_pages("/docs", params, limit=limit)
    
    def get_doc(self, doc_id: str) -> Dict[str, Any]:
        """
        Get metadata for a specific doc.
        
        Args:
            doc_id: ID of the doc
            
        Returns:
            Doc metadata
        """
        return self._get(f"/docs/{doc_id}")
    
    def create_doc(
        self,
        title: Optional[str] = None,
        source_doc: Optional[str] = None,
        timezone: Optional[str] = None,
        folder_id: Optional[str] = None,
        initial_page: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a new Coda doc.
        
        Args:
            title: Doc title (default: 'Untitled')
            source_doc: Doc ID to copy from
            timezone: Timezone for the doc
            folder_id: Folder to create in
            initial_page: Initial page content
            
        Returns:
            Created doc metadata with requestId
        """
        data = {}
        if title:
            data["title"] = title
        if source_doc:
            data["sourceDoc"] = source_doc
        if timezone:
            data["timezone"] = timezone
        if folder_id:
            data["folderId"] = folder_id
        if initial_page:
            data["initialPage"] = initial_page
        
        return self._post("/docs", data=data)
    
    def update_doc(
        self,
        doc_id: str,
        title: Optional[str] = None,
        icon_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update doc metadata.
        
        Args:
            doc_id: ID of the doc
            title: New title
            icon_name: New icon name
            
        Returns:
            Update result
        """
        data = {}
        if title:
            data["title"] = title
        if icon_name:
            data["iconName"] = icon_name
        
        return self._patch(f"/docs/{doc_id}", data=data)
    
    def delete_doc(self, doc_id: str) -> Dict[str, Any]:
        """
        Delete a doc.
        
        Args:
            doc_id: ID of the doc to delete
            
        Returns:
            Deletion result
        """
        return self._delete(f"/docs/{doc_id}")
    
    # -------------------------------------------------------------------------
    # Mutation Status
    # -------------------------------------------------------------------------
    
    def get_mutation_status(self, request_id: str) -> Dict[str, Any]:
        """
        Check the status of an async mutation.
        
        Args:
            request_id: ID from a mutation response
            
        Returns:
            Status with 'completed' boolean
        """
        return self._get(f"/mutationStatus/{request_id}")
    
    # -------------------------------------------------------------------------
    # Resolve Browser Link
    # -------------------------------------------------------------------------
    
    def resolve_browser_link(
        self,
        url: str,
        degrade_gracefully: bool = False
    ) -> Dict[str, Any]:
        """
        Resolve a Coda browser URL to API metadata.
        
        Args:
            url: Browser link to resolve
            degrade_gracefully: Return parent if object deleted
            
        Returns:
            Resolved resource metadata
        """
        params = {
            "url": url,
            "degradeGracefully": degrade_gracefully
        }
        return self._get("/resolveBrowserLink", params=params)
