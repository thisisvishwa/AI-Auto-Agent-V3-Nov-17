```javascript
import dynamic from 'next/dynamic';

// Dynamically import modules for code splitting
const OpenAIComponent = dynamic(() => import('../components/OpenAIComponent'));
const PalmAPIComponent = dynamic(() => import('../components/PalmAPIComponent'));
const ClaudeComponent = dynamic(() => import('../components/ClaudeComponent'));

function HomePage() {
  return (
    <div>
      <OpenAIComponent />
      <PalmAPIComponent />
      <ClaudeComponent />
    </div>
  );
}

export default HomePage;
```