from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional
import logging

class GoogleGeminiClient(UniversalGoogleClient):
    """
    Client for the Google Generative Language API (Gemini).
    Enhanced with comprehensive convenience methods for:
    - Model information and listing
    - Text content generation
    - Multi-turn conversations
    - Embeddings
    - Token counting
    - Safety and generation configuration
    """
    def __init__(self):
        super().__init__(service_name='generativelanguage', version='v1beta')

    # =====================
    # Model Information
    # =====================

    def list_models(self) -> List[Dict[str, Any]]:
        """List all available Gemini models with their capabilities."""
        if not self.is_ready():
            return []
        result = self.service.models().list().execute()
        return result.get("models", [])

    def get_model(self, model_name: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a specific model.
        
        Args:
            model_name: Model name (e.g., 'models/gemini-1.5-flash')
        """
        if not self.is_ready():
            return None
        try:
            return self.service.models().get(name=model_name).execute()
        except Exception as e:
            logging.error(f"Error getting model {model_name}: {e}")
            return None

    # =====================
    # Content Generation
    # =====================

    def generate_content(self, model: str, contents: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        Generate content using a Gemini model.
        
        Args:
            model: Full model path (e.g., 'models/gemini-1.5-flash')
            contents: List of content dicts with 'role' and 'parts' keys
                     e.g., [{'role': 'user', 'parts': [{'text': 'Hello!'}]}]
        """
        if not self.is_ready():
            return None
        return self.service.models().generateContent(
            model=model,
            body={"contents": contents}
        ).execute()

    def generate_text(self, prompt: str, model: str = 'models/gemini-1.5-flash',
                      temperature: float = 0.7, max_output_tokens: int = 2048) -> Optional[str]:
        """
        Generate text from a simple prompt - convenience method.
        
        Args:
            prompt: The text prompt
            model: Model to use
            temperature: Creativity (0.0-1.0)
            max_output_tokens: Maximum tokens in response
        
        Returns:
            Generated text string or None on error
        """
        if not self.is_ready():
            return None
        
        body = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_output_tokens
            }
        }
        
        try:
            response = self.service.models().generateContent(
                model=model,
                body=body
            ).execute()
            
            # Extract text from response
            candidates = response.get('candidates', [])
            if candidates and candidates[0].get('content', {}).get('parts'):
                return candidates[0]['content']['parts'][0].get('text', '')
            return None
        except Exception as e:
            logging.error(f"Error generating text: {e}")
            return None

    def generate_text_with_history(self, messages: List[Dict[str, str]], 
                                   model: str = 'models/gemini-1.5-flash',
                                   temperature: float = 0.7) -> Optional[str]:
        """
        Generate text with conversation history.
        
        Args:
            messages: List of dicts with 'role' ('user' or 'model') and 'text' keys
            model: Model to use
            temperature: Creativity setting
        """
        if not self.is_ready():
            return None
        
        contents = []
        for msg in messages:
            contents.append({
                "role": msg.get('role', 'user'),
                "parts": [{"text": msg['text']}]
            })
        
        body = {
            "contents": contents,
            "generationConfig": {
                "temperature": temperature
            }
        }
        
        try:
            response = self.service.models().generateContent(
                model=model,
                body=body
            ).execute()
            
            candidates = response.get('candidates', [])
            if candidates and candidates[0].get('content', {}).get('parts'):
                return candidates[0]['content']['parts'][0].get('text', '')
            return None
        except Exception as e:
            logging.error(f"Error in multi-turn generation: {e}")
            return None

    def generate_with_safety_settings(self, prompt: str, 
                                       safety_settings: List[Dict[str, str]],
                                       model: str = 'models/gemini-1.5-flash') -> Optional[Dict[str, Any]]:
        """
        Generate content with custom safety settings.
        
        Args:
            prompt: The text prompt
            safety_settings: List of dicts with 'category' and 'threshold' keys
                e.g., [{'category': 'HARM_CATEGORY_HARASSMENT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'}]
        """
        if not self.is_ready():
            return None
        
        body = {
            "contents": [{"parts": [{"text": prompt}]}],
            "safetySettings": safety_settings
        }
        
        try:
            return self.service.models().generateContent(
                model=model,
                body=body
            ).execute()
        except Exception as e:
            logging.error(f"Error with safety settings: {e}")
            return None

    def generate_with_config(self, prompt: str, generation_config: Dict[str, Any],
                             model: str = 'models/gemini-1.5-flash') -> Optional[Dict[str, Any]]:
        """
        Generate content with custom generation configuration.
        
        Args:
            prompt: The text prompt
            generation_config: Dict with config options like:
                - 'temperature': 0.0-1.0
                - 'topP': 0.0-1.0
                - 'topK': int
                - 'maxOutputTokens': int
                - 'stopSequences': list of strings
        """
        if not self.is_ready():
            return None
        
        body = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": generation_config
        }
        
        try:
            return self.service.models().generateContent(
                model=model,
                body=body
            ).execute()
        except Exception as e:
            logging.error(f"Error with generation config: {e}")
            return None

    # =====================
    # Token Counting
    # =====================

    def count_tokens(self, contents: List[Dict[str, Any]], 
                     model: str = 'models/gemini-1.5-flash') -> int:
        """
        Count tokens in content.
        
        Args:
            contents: List of content dicts (same format as generate_content)
            model: Model to use for tokenization
        
        Returns:
            Token count or -1 on error
        """
        if not self.is_ready():
            return -1
        
        try:
            response = self.service.models().countTokens(
                model=model,
                body={"contents": contents}
            ).execute()
            return response.get('totalTokens', -1)
        except Exception as e:
            logging.error(f"Error counting tokens: {e}")
            return -1

    def count_text_tokens(self, text: str, model: str = 'models/gemini-1.5-flash') -> int:
        """Count tokens in a text string - convenience method."""
        contents = [{"parts": [{"text": text}]}]
        return self.count_tokens(contents, model)

    # =====================
    # Embeddings
    # =====================

    def embed_content(self, text: str, model: str = 'models/embedding-001',
                      task_type: str = 'RETRIEVAL_DOCUMENT') -> List[float]:
        """
        Generate embeddings for text content.
        
        Args:
            text: Text to embed
            model: Embedding model to use
            task_type: One of:
                - 'RETRIEVAL_QUERY': For search queries
                - 'RETRIEVAL_DOCUMENT': For documents to be searched
                - 'SEMANTIC_SIMILARITY': For comparing text similarity
                - 'CLASSIFICATION': For text classification
                - 'CLUSTERING': For clustering text
        
        Returns:
            List of embedding floats or empty list on error
        """
        if not self.is_ready():
            return []
        
        try:
            body = {
                "content": {"parts": [{"text": text}]},
                "taskType": task_type
            }
            response = self.service.models().embedContent(
                model=model,
                body=body
            ).execute()
            return response.get('embedding', {}).get('values', [])
        except Exception as e:
            logging.error(f"Error generating embedding: {e}")
            return []

    def batch_embed_contents(self, texts: List[str], 
                             model: str = 'models/embedding-001',
                             task_type: str = 'RETRIEVAL_DOCUMENT') -> List[List[float]]:
        """
        Generate embeddings for multiple texts in a single request.
        
        Returns:
            List of embedding vectors
        """
        if not self.is_ready():
            return []
        
        try:
            requests = []
            for text in texts:
                requests.append({
                    "model": model,
                    "content": {"parts": [{"text": text}]},
                    "taskType": task_type
                })
            
            body = {"requests": requests}
            response = self.service.models().batchEmbedContents(
                model=model,
                body=body
            ).execute()
            
            embeddings = response.get('embeddings', [])
            return [e.get('values', []) for e in embeddings]
        except Exception as e:
            logging.error(f"Error in batch embedding: {e}")
            return []

    # =====================
    # Chat Sessions
    # =====================

    def create_chat_session(self, history: Optional[List[Dict[str, str]]] = None,
                            model: str = 'models/gemini-1.5-flash') -> Dict[str, Any]:
        """
        Create a chat session object for multi-turn conversations.
        
        Args:
            history: Optional list of prior messages (role/text dicts)
            model: Model to use
        
        Returns:
            Chat session dict to pass to send_chat_message
        """
        formatted_history = []
        if history:
            for msg in history:
                formatted_history.append({
                    "role": msg.get('role', 'user'),
                    "parts": [{"text": msg['text']}]
                })
        
        return {
            "model": model,
            "history": formatted_history
        }

    def send_chat_message(self, session: Dict[str, Any], message: str,
                          temperature: float = 0.7) -> Optional[str]:
        """
        Send a message in a chat session and get a response.
        Updates the session history in-place.
        
        Args:
            session: Chat session from create_chat_session
            message: User message text
            temperature: Creativity setting
        
        Returns:
            Model response text or None on error
        """
        if not self.is_ready():
            return None
        
        # Add user message to history
        session['history'].append({
            "role": "user",
            "parts": [{"text": message}]
        })
        
        body = {
            "contents": session['history'],
            "generationConfig": {
                "temperature": temperature
            }
        }
        
        try:
            response = self.service.models().generateContent(
                model=session['model'],
                body=body
            ).execute()
            
            candidates = response.get('candidates', [])
            if candidates and candidates[0].get('content', {}).get('parts'):
                response_text = candidates[0]['content']['parts'][0].get('text', '')
                # Add model response to history
                session['history'].append({
                    "role": "model",
                    "parts": [{"text": response_text}]
                })
                return response_text
            return None
        except Exception as e:
            logging.error(f"Error in chat: {e}")
            # Remove failed user message from history
            session['history'].pop()
            return None
