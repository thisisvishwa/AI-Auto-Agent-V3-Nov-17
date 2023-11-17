```javascript
import { useState, useEffect } from 'react';
import axios from 'axios';

const AsynchronousOperationsHandler = () => {
  const [appState, setAppState] = useState({
    loading: false,
    data: null,
  });

  useEffect(() => {
    setAppState({ loading: true });
    const apiUrl = `https://api.example.com/data`;
    axios.get(apiUrl).then((response) => {
      const allData = response.data;
      setAppState({ loading: false, data: allData });
    });
  }, [setAppState]);

  return (
    <div>
      {appState.loading ? (
        <div>Loading...</div>
      ) : (
        <div>
          <h2>{appState.data.title}</h2>
          <p>{appState.data.description}</p>
        </div>
      )}
    </div>
  );
};

export default AsynchronousOperationsHandler;
```