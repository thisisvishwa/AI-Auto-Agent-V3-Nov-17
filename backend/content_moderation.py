```python
import requests
import json

claude_api_key = "your_claude_api_key"

def moderateContent(text):
    url = "https://api.claude.ai/v1/moderate"
    headers = {
        "Authorization": f"Bearer {claude_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        if result["is_safe"]:
            return text
        else:
            return "Content is not safe for display."
    else:
        raise Exception(f"Content moderation failed with status code {response.status_code}")
```