import json
import os
import subprocess
import threading
import time
import sys
from typing import Dict, Any, List, Optional

class GoogleMCPClient:
    """
    A base Python client that interfaces with an MCP server via stdio.
    """
    
    def __init__(self, 
                 server_command: List[str],
                 env: Optional[Dict[str, str]] = None,
                 cwd: Optional[str] = None):
        """
        Initialize the client and start the MCP server subprocess.
        """
        self.server_command = server_command
        self.env = env or os.environ.copy()
        self.cwd = cwd
        self.lock = threading.Lock()
        self.request_id = 0
        self.pending_requests: Dict[int, Any] = {}
        self.process: Optional[subprocess.Popen] = None
        self.listening = False
        
        # Start the server
        self._start_server()

    def _start_server(self):
        # Force encoding to UTF-8
        self.env["PYTHONIOENCODING"] = "utf-8"

        print(f"Starting MCP server: {' '.join(self.server_command)}")
        self.process = subprocess.Popen(
            self.server_command,
            env=self.env,
            cwd=self.cwd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1  # Line buffered
        )
        
        self.listening = True
        self.listener_thread = threading.Thread(target=self._listen_stdout)
        self.listener_thread.daemon = True
        self.listener_thread.start()
        
        self.stderr_thread = threading.Thread(target=self._listen_stderr)
        self.stderr_thread.daemon = True
        self.stderr_thread.start()
        
        # Initialize handshake
        self._initialize()

    def _listen_stdout(self):
        """Read stdout from the server line by line."""
        while self.listening and self.process:
            try:
                line = self.process.stdout.readline()
                if not line:
                    break
                line = line.strip()
                if not line:
                    continue
                
                try:
                    msg = json.loads(line)
                    self._handle_message(msg)
                except json.JSONDecodeError:
                    # Ignore non-JSON output (logs)
                    pass
            except Exception as e:
                print(f"Error reading stdout: {e}")
                break

    def _listen_stderr(self):
        """Read stderr for logging."""
        while self.listening and self.process:
            try:
                line = self.process.stderr.readline()
                if not line:
                    break
                print(f"MCP LOG: {line.strip()}", file=sys.stderr)
            except Exception:
                break

    def _handle_message(self, msg: Dict[str, Any]):
        """Handle incoming JSON-RPC messages."""
        if "id" in msg and msg["id"] in self.pending_requests:
            # Response to a request
            req_id = msg["id"]
            future, _ = self.pending_requests.pop(req_id)
            if "error" in msg:
                future.set_exception(Exception(f"RPC Error: {msg['error']}"))
            else:
                future.set_result(msg.get("result"))

    def _send_request(self, method: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Send a JSON-RPC request and wait for the response."""
        with self.lock:
            req_id = self.request_id
            self.request_id += 1
        
        msg = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params or {}
        }
        
        response_container = {"result": None, "error": None, "done": threading.Event()}
        
        class Future:
            def set_result(self, res):
                response_container["result"] = res
                response_container["done"].set()
            def set_exception(self, exc):
                response_container["error"] = exc
                response_container["done"].set()
                
        self.pending_requests[req_id] = (Future(), msg)
        
        if self.process and self.process.stdin:
            try:
                self.process.stdin.write(json.dumps(msg) + "\n")
                self.process.stdin.flush()
            except BrokenPipeError:
                raise RuntimeError("MCP Server process died")
        else:
            raise RuntimeError("MCP Client process is not running")
            
        # Wait for response with timeout
        if not response_container["done"].wait(timeout=60):
            if req_id in self.pending_requests:
                del self.pending_requests[req_id]
            raise TimeoutError(f"Request {method} timed out")
            
        if response_container["error"]:
            raise response_container["error"]
            
        return response_container["result"]

    def _initialize(self):
        """Perform MCP initialization handshake."""
        # 1. Initialize
        res = self._send_request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "roots": {"listChanged": True},
                "sampling": {}
            },
            "clientInfo": {"name": "PAI-Python-Client", "version": "1.0.0"}
        })
        
        if not res:
            raise RuntimeError("Failed to initialize MCP connection")
            
        # 2. Notify initialized
        msg = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized",
            "params": {}
        }
        if self.process and self.process.stdin:
            self.process.stdin.write(json.dumps(msg) + "\n")
            self.process.stdin.flush()

    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Generic method to call an MCP tool."""
        res = self._send_request("tools/call", {
            "name": tool_name,
            "arguments": arguments
        })
        
        if res and "content" in res:
            # MCP returns content list, usually we want the text or json from the first item
            content = res["content"]
            if isinstance(content, list) and len(content) > 0:
                item = content[0]
                if item.get("type") == "text":
                    try:
                        return json.loads(item["text"])
                    except json.JSONDecodeError:
                        return item["text"]
        return res

    def close(self):
        """Terminate the client connection."""
        self.listening = False
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except Exception:
                pass

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
