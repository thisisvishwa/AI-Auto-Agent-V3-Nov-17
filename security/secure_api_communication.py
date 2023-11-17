```python
import requests
from requests.structures import CaseInsensitiveDict

def secureAPICommunication(url, headers, data, method):
    # Ensure headers are case-insensitive
    headers = CaseInsensitiveDict(headers)

    # Add the API keys to the headers
    headers["OpenAI-API-Key"] = openai_api_key
    headers["Palm-API-Key"] = palm_api_key
    headers["Claude-API-Key"] = claude_api_key

    # Use the appropriate HTTP method
    if method.lower() == "get":
        response = requests.get(url, headers=headers)
    elif method.lower() == "post":
        response = requests.post(url, headers=headers, json=data)
    elif method.lower() == "put":
        response = requests.put(url, headers=headers, json=data)
    elif method.lower() == "delete":
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError(f"Invalid HTTP method: {method}")

    # Check for successful request
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")

    return response.json()
```