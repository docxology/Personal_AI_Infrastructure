import os
import sys
import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import threading

# Python adds the script directory to sys.path[0]. This causes the local 'calendar' package
# to shadow the standard library 'calendar' module, breaking 'requests' and other libs.
# We must remove it.
script_dir = os.path.dirname(os.path.abspath(__file__))
if sys.path and sys.path[0] == script_dir:
    sys.path.pop(0)

# Add src to path
sys.path.append(os.path.abspath(os.path.join(script_dir, '../../src')))

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    print("Please run: pip install google-auth-oauthlib requests")
    sys.exit(1)

from google.utils import get_base_credentials_path, get_base_token_path

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/tasks"
]

def setup_auth():
    creds_path = get_base_credentials_path()
    token_path = get_base_token_path()
    
    logging.info(f"Credentials Path: {creds_path}")
    logging.info(f"Token Path: {token_path}")
    
    if not os.path.exists(creds_path):
        logging.error(f"Error: Credentials file not found at {creds_path}")
        return

    logging.info("Starting Authentication Flow...")
    flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
    # Explicitly set the redirect URI to match credentials.json
    flow.redirect_uri = "http://localhost:3500/oauth2callback"
    
    auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
    
    logging.info(f"\nPlease visit this URL to authorize: {auth_url}\n")
    
    done_event = threading.Event()
    
    class OAuthHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path.startswith("/oauth2callback"):
                query = urlparse(self.path).query
                params = parse_qs(query)
                code = params.get('code', [None])[0]
                error = params.get('error', [None])[0]
                
                if code:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b"<h1>Authentication successful!</h1><p>You can close this window.</p>")
                    
                    logging.info(f"Received auth code: {code[:10]}...")
                    try:
                        flow.fetch_token(code=code)
                        with open(token_path, 'w') as token:
                            token.write(flow.credentials.to_json())
                        logging.info(f"Successfully saved new token to {token_path}")
                    except Exception as e:
                        logging.error(f"Error fetching token: {e}")
                    
                    done_event.set()
                else:
                    self.send_response(400)
                    self.wfile.write(b"Authentication failed or cancelled.")
                    logging.error(f"Auth failed: {error}")
                    done_event.set()
            else:
                self.send_response(404)
                self.end_headers()

    server = HTTPServer(('localhost', 3500), OAuthHandler)
    logging.info("Listening on http://localhost:3500/oauth2callback ...")
    
    server.timeout = 1
    while not done_event.is_set():
        server.handle_request()

    logging.info("Exiting auth script.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    setup_auth()
