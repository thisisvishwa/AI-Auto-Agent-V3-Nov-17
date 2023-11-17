```javascript
import dynamic from 'next/dynamic';

// Lazy load AIOutput component
const AIOutput = dynamic(() => import('../components/AIOutput'), {
  loading: () => <p>Loading...</p>,
  ssr: false
});

// Lazy load UserInput component
const UserInput = dynamic(() => import('../components/UserInput'), {
  loading: () => <p>Loading...</p>,
  ssr: false
});

// Lazy load TransactionData component
const TransactionData = dynamic(() => import('../components/TransactionData'), {
  loading: () => <p>Loading...</p>,
  ssr: false
});

function App() {
  return (
    <div>
      <AIOutput />
      <UserInput />
      <TransactionData />
    </div>
  );
}

export default App;
```