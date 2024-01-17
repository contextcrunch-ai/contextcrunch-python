from typing import List, Literal, Optional, Union

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
            if response.status_code == 401:
                raise Exception("Invalid API key")
            elif response.status_code == 402:
                raise Exception("Insufficient funds. Please add more at https://contextcrunch.com/console/billing")
            return response.json()
        except Exception as e:
            raise Exception(f"Error making request to {request_url}: {e}")
            
    
    def compress(self, context: Union[str,List[str]], prompt: str, compression_ratio=0.9, type: Optional[Literal['rag', 'conversation']] = 'rag', concat_prompt = False):
        if compression_ratio < 0.5 or compression_ratio > 0.999 :
            raise Exception("Compression ratio must be between 0.5 and 0.999")
        if type not in ['rag', 'conversation']:
            raise Exception("Type must be either 'rag' or 'conversation'")
        if not isinstance(prompt, str):
            raise Exception("Prompt must be a string")
        if isinstance(context, str):
            context = [context]
        if not isinstance(context, list):
            raise Exception("Context must be a list of strings (or a single string)")
        body = {
            "input": {
                "context": context,
                "prompt": prompt,
                "compression_ratio": compression_ratio,
                "type": type
            }
        }
        result = self._request("call", body)
        if concat_prompt:
            return f'{result["output"]}\n\n{prompt}'
        return result['output']
        