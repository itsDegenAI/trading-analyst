
import json
import os

class TokenContextBuilder:
    def __init__(self, db_path="tokens.json"):
        self.db_path = db_path
        self.tokens = {}

    def load_tokens(self):
        if os.path.exists(self.db_path):
            with open(self.db_path) as f:
                self.tokens = json.load(f)

    def enrich(self, token):
        info = self.tokens.get(token, {})
        return {
            "symbol": info.get("symbol", token),
            "verified": info.get("verified", False),
            "launch_timestamp": info.get("created", "unknown")
        }
