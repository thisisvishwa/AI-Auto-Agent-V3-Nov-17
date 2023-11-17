```javascript
import { useState } from 'react';
import { manageState } from './state_management';
import { fetchData } from './data_fetching';
import { generateText, summarizeText, translateText } from '../backend/openai_integration';

const UserFlow = () => {
  const [userInput, setUserInput] = useState('');
  const [aiOutput, setAiOutput] = useState('');
  const [transactionData, setTransactionData] = useState(null);

  const handleUserQuery = async (query) => {
    setUserInput(query);
    const aiResponse = await generateText(query);
    setAiOutput(aiResponse);
    manageState('USER_QUERY', query);
    manageState('AI_RESPONSE', aiResponse);
  };

  const handleTransactionUpdate = async (transaction) => {
    const updatedData = await fetchData(transaction);
    setTransactionData(updatedData);
    manageState('TRANSACTION_UPDATE', updatedData);
  };

  return (
    <div>
      <input
        id="user-input"
        type="text"
        value={userInput}
        onChange={(e) => handleUserQuery(e.target.value)}
      />
      <div id="ai-output">{aiOutput}</div>
      <div id="transaction-data">{transactionData}</div>
    </div>
  );
};

export default UserFlow;
```