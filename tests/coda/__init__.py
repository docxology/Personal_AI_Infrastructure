"""
Coda Tests Package
"""
import os
import sys
import unittest

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

PAI_DOC_ID = "NDxZHneeIw"

def has_coda_token() -> bool:
    if os.environ.get("CODA_API_TOKEN"):
        return True
    return os.path.exists(os.path.expanduser("~/.claude/coda/token.json"))

skip_without_token = lambda cls: unittest.skipUnless(has_coda_token(), "No token")(cls)
