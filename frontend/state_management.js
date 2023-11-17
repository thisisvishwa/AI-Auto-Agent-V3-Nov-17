```javascript
import { useState, useEffect } from 'react';

// Initial state
const initialState = {
  user: {},
  aiOutput: {},
  transactionData: {},
};

// State management using React Hooks
const useAppState = () => {
  const [appState, setAppState] = useState(initialState);

  // Function to manage state
  const manageState = (newState) => {
    setAppState(prevState => ({ ...prevState, ...newState }));
  };

  return { appState, manageState };
};

// Fetching data from backend
const fetchData = async () => {
  const response = await fetch('/api/data');
  const data = await response.json();
  manageState(data);
};

// Handling asynchronous operations
useEffect(() => {
  fetchData();
}, []);

export default useAppState;
```