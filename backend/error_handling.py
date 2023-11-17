```python
import logging
import openai
from openai.api_resources.abstract.api_resource import APIResource

# Initialize logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Set OpenAI API key
openai.api_key = 'openai_api_key'

def handle_openai_errors(func):
    """
    Decorator function to handle errors from OpenAI API
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except openai.error.OpenAIError as e:
            logging.error(f"OpenAIError: {str(e)}")
        except openai.error.InvalidRequestError as e:
            logging.error(f"InvalidRequestError: {str(e)}")
        except openai.error.AuthenticationError as e:
            logging.error(f"AuthenticationError: {str(e)}")
        except openai.error.APIConnectionError as e:
            logging.error(f"APIConnectionError: {str(e)}")
        except openai.error.RateLimitError as e:
            logging.error(f"RateLimitError: {str(e)}")
        except Exception as e:
            logging.error(f"Unexpected Error: {str(e)}")
    return wrapper

@handle_openai_errors
def generate_text(prompt):
    """
    Function to generate text using OpenAI
    """
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

@handle_openai_errors
def summarize_text(text):
    """
    Function to summarize text using OpenAI
    """
    response = openai.Completion.create(engine="text-davinci-002", prompt=f"{text}\n\nSummarize:", max_tokens=100)
    return response.choices[0].text.strip()

@handle_openai_errors
def translate_text(text, target_language):
    """
    Function to translate text using OpenAI
    """
    response = openai.Completion.create(engine="text-davinci-002", prompt=f"{text}\n\nTranslate to {target_language}:", max_tokens=100)
    return response.choices[0].text.strip()
```