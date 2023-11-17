```python
import requests
import json

claude_api_key = "your_claude_api_key"

def predictModel(input_data):
    url = "https://api.claude.ai/predict"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {claude_api_key}"
    }

    data = {
        "input": input_data
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed with status {response.status_code}")
```