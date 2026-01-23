from google.universal_client import UniversalGoogleClient
from typing import Dict, Any, Optional, List

class GoogleGeminiForGoogleWorkspaceClient(UniversalGoogleClient):
    """
    Client for Gemini for Google Workspace integration.
    
    Note: Gemini for Google Workspace features (Docs, Sheets, Slides, Gmail AI) 
    are accessed through the respective Workspace application APIs, not a dedicated 
    Gemini Workspace API. This client provides utilities to:
    
    1. Check Gemini availability in Workspace applications
    2. Provide Workspace context for Gemini generation via the main Gemini client
    3. Helper methods for common Workspace AI patterns
    
    For direct Gemini API access, use GoogleGeminiClient instead.
    For Workspace application APIs, use respective clients (Docs, Sheets, etc.)
    """
    def __init__(self, service_name='admin', version='reports_v1'):
        # Use Admin SDK for Workspace usage analytics
        # Note: Requires admin privileges
        super().__init__(service_name=service_name, version=version)
        self._workspace_context = {}

    def set_workspace_context(self, context: Dict[str, Any]) -> None:
        """
        Set workspace context for Gemini operations.
        
        Args:
            context: Dict with workspace-specific context like:
                - 'document_id': ID of current Workspace document
                - 'document_type': 'doc', 'sheet', 'slide', 'email'
                - 'user_email': User's workspace email
                - 'organization': Workspace organization
        """
        self._workspace_context = context

    def get_workspace_context(self) -> Dict[str, Any]:
        """Get current workspace context."""
        return self._workspace_context.copy()

    def format_for_workspace(self, prompt: str, document_content: str = '',
                              document_type: str = 'doc') -> str:
        """
        Format a prompt with workspace context for better Gemini responses.
        
        Args:
            prompt: The user's prompt/question
            document_content: Content from the Workspace document
            document_type: Type of document (doc, sheet, slide, email)
        
        Returns:
            Formatted prompt with workspace context
        """
        context_header = f"Context: Working with a Google {document_type.title()}\n"
        
        if document_content:
            context_header += f"Document content:\n---\n{document_content[:4000]}\n---\n\n"
        
        if self._workspace_context:
            if 'organization' in self._workspace_context:
                context_header += f"Organization: {self._workspace_context['organization']}\n"
        
        return f"{context_header}User request: {prompt}"

    def build_doc_assistance_prompt(self, action: str, selection: str = '', 
                                     style: str = 'professional') -> str:
        """
        Build a prompt for Google Docs assistance.
        
        Args:
            action: What to do - 'summarize', 'expand', 'rewrite', 'proofread', 'simplify'
            selection: Selected text from the document
            style: Writing style - 'professional', 'casual', 'academic', 'creative'
        """
        action_prompts = {
            'summarize': f"Summarize the following text in a {style} tone:\n\n{selection}",
            'expand': f"Expand on this text with more detail in a {style} tone:\n\n{selection}",
            'rewrite': f"Rewrite this text in a {style} tone:\n\n{selection}",
            'proofread': f"Proofread and fix any errors in this text:\n\n{selection}",
            'simplify': f"Simplify this text to make it easier to understand:\n\n{selection}"
        }
        return action_prompts.get(action, f"{action}: {selection}")

    def build_sheet_analysis_prompt(self, data_description: str, 
                                     question: str) -> str:
        """
        Build a prompt for Google Sheets data analysis.
        
        Args:
            data_description: Description of the spreadsheet data (headers, sample rows)
            question: User's analysis question
        """
        return (
            f"I have a Google Sheets spreadsheet with the following structure:\n"
            f"{data_description}\n\n"
            f"Please help me with this question: {question}\n\n"
            f"Provide your analysis and any suggested formulas if applicable."
        )

    def build_email_draft_prompt(self, context: str, tone: str = 'professional',
                                  reply_to: str = '') -> str:
        """
        Build a prompt for Gmail drafting assistance.
        
        Args:
            context: What the email should be about
            tone: Email tone - 'professional', 'friendly', 'formal', 'brief'
            reply_to: Original email content if replying
        """
        if reply_to:
            return (
                f"Draft a {tone} reply to this email:\n\n"
                f"---Original email---\n{reply_to}\n---\n\n"
                f"My response should convey: {context}"
            )
        return f"Draft a {tone} email about: {context}"

    def build_slides_prompt(self, action: str, content: str = '') -> str:
        """
        Build a prompt for Google Slides assistance.
        
        Args:
            action: What to do - 'outline', 'speaker_notes', 'improve', 'summarize'
            content: Slide content or topic
        """
        action_prompts = {
            'outline': (
                f"Create a presentation outline for the topic: {content}\n"
                "Include suggested slide titles and key bullet points."
            ),
            'speaker_notes': (
                f"Write speaker notes for a slide with this content:\n{content}"
            ),
            'improve': (
                f"Suggest improvements for this slide content:\n{content}"
            ),
            'summarize': (
                f"Create a summary slide based on this presentation content:\n{content}"
            )
        }
        return action_prompts.get(action, f"{action}: {content}")

    def get_gemini_features_info(self) -> Dict[str, Any]:
        """
        Get information about Gemini for Workspace features.
        
        Returns dict with feature availability info. Note: This is informational;
        actual feature availability depends on Workspace subscription level.
        """
        return {
            'available_in_apps': [
                'Google Docs - Help me write, summarize, rewrite',
                'Google Sheets - Help me organize, create formulas, analyze',
                'Google Slides - Create image, help me visualize, speaker notes',
                'Gmail - Help me write, polish, summarize emails',
                'Google Meet - Take notes, generate summaries',
                'Google Chat - Summarize conversations'
            ],
            'requirements': [
                'Google Workspace Business, Enterprise, or Education subscription',
                'Gemini for Workspace add-on enabled by admin',
                'User must be 18+'
            ],
            'integration_pattern': (
                "Use the main Gemini API (GoogleGeminiClient) with workspace context "
                "for AI-powered assistance. This client provides prompt templates and "
                "helpers optimized for Workspace use cases."
            )
        }

