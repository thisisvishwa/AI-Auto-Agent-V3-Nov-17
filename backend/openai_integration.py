```python
import openai
import logging
from cachetools import cached, TTLCache

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up cache (TTL = 1 hour)
cache = TTLCache(maxsize=100, ttl=3600)

# Set up OpenAI API
openai.api_key = openai_api_key

@cached(cache)
def generateText(prompt, max_tokens=100):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error in generateText: {e}")
        return None

@cached(cache)
def summarizeText(document):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=document,
            temperature=0.3,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error in summarizeText: {e}")
        return None

@cached(cache)
def translateText(text, source_lang, target_lang):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{source_lang}:{text}\n{target_lang}:",
            max_tokens=60
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error in translateText: {e}")
        return None
```