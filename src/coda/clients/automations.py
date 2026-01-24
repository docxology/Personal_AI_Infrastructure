"""
Coda Automations Client

Webhook automation triggers.
"""

from typing import Dict, Any, Optional
from coda.core.base_client import CodaClient


class CodaAutomationsClient(CodaClient):
    """
    Client for Coda automation operations.
    """
    
    def trigger_automation(
        self,
        doc_id: str,
        rule_id: str,
        payload: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Trigger a webhook-invoked automation.
        
        Args:
            doc_id: ID of the doc
            rule_id: ID of the automation rule (e.g., grid-auto-xyz)
            payload: JSON payload to send to the automation
            
        Returns:
            Result with requestId
        """
        return self._post(
            f"/docs/{doc_id}/hooks/automation/{rule_id}",
            data=payload or {}
        )
    
    def trigger_with_message(
        self,
        doc_id: str,
        rule_id: str,
        message: str
    ) -> Dict[str, Any]:
        """
        Trigger an automation with a simple message.
        
        Args:
            doc_id: ID of the doc
            rule_id: Automation rule ID
            message: Message string to send
            
        Returns:
            Result with requestId
        """
        return self.trigger_automation(doc_id, rule_id, {"message": message})
