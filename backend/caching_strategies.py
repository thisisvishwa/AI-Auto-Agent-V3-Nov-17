```python
import requests
from cachetools import cached, TTLCache

# Define cache size and time-to-live (in seconds)
cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def generateText(openai_api_key, text):
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers={"Authorization": f"Bearer {openai_api_key}"},
        json={"prompt": text, "max_tokens": 60},
    )
    return response.json()

@cached(cache)
def summarizeText(openai_api_key, text):
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers={"Authorization": f"Bearer {openai_api_key}"},
        json={"prompt": f"Summarize: {text}", "max_tokens": 60},
    )
    return response.json()

@cached(cache)
def translateText(openai_api_key, text, target_language):
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers={"Authorization": f"Bearer {openai_api_key}"},
        json={"prompt": f"Translate English to {target_language}: {text}", "max_tokens": 60},
    )
    return response.json()
```