from typing import List

import requests


class ContextCrunchClient: 
    def __init__(self, api_key, url="https://contextcrunch.com/api"):
        self.api_key = api_key
        self.url = url
        if not self.api_key:
            raise Exception("No API key provided")
        
    def _request(self, endpoint, data) -> dict:
        header = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        request_url = f"{self.url}/{endpoint}"
        try:
            response = requests.post(request_url, headers=header, json=data)
            return response.json()
        except Exception as e:
            raise Exception(f"Error making request to {request_url}: {e}")
            
    
    def compress(self, context: List[str], prompt: str, compression_ratio=0.9):
        if compression_ratio <= 0 or compression_ratio >= 1 :
            raise Exception("Compression ratio must be between 0 and 1 (exclusive)")
        body = {
            "input": {
                "context": context,
                "prompt": prompt,
                "compression_ratio": compression_ratio
            }
        }
        result = self._request("call", body)
        return result['output']
        