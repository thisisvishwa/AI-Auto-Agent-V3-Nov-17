```javascript
import axios from 'axios';

// Define the base URL for the API
const API_BASE_URL = 'http://localhost:5000/api';

// Define the endpoints
const OPENAI_ENDPOINT = `${API_BASE_URL}/openai`;
const PALM_ENDPOINT = `${API_BASE_URL}/palm`;
const CLAUDE_ENDPOINT = `${API_BASE_URL}/claude`;

// Function to fetch data from OpenAI
export async function fetchDataFromOpenAI(query) {
  try {
    const response = await axios.post(OPENAI_ENDPOINT, { query });
    return response.data;
  } catch (error) {
    console.error('Error fetching data from OpenAI:', error);
  }
}

// Function to fetch data from Palm API
export async function fetchDataFromPalm(transactionId) {
  try {
    const response = await axios.get(`${PALM_ENDPOINT}/${transactionId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching data from Palm API:', error);
  }
}

// Function to fetch data from Claude
export async function fetchDataFromClaude(content) {
  try {
    const response = await axios.post(CLAUDE_ENDPOINT, { content });
    return response.data;
  } catch (error) {
    console.error('Error fetching data from Claude:', error);
  }
}
```