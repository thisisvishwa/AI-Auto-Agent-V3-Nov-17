```python
import requests
import json

claude_api_key = "your_claude_api_key_here"

def analyzeSentiment(text):
    url = "https://api.claude.ai/sentiment"
    headers = {
        "Authorization": f"Bearer {claude_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        sentiment = response.json()
        return sentiment
    else:
        raise Exception(f"Request to Claude API failed with status {response.status_code}.")
```
This Python script uses the Claude API to perform sentiment analysis on a given text. The `analyzeSentiment` function takes a text string as input, sends a POST request to the Claude API, and returns the sentiment analysis result. If the request fails, it raises an exception with the status code of the failed request.