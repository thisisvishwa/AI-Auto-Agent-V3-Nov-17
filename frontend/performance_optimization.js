```javascript
import dynamic from 'next/dynamic';
import { useEffect, useState } from 'react';

// Lazy load heavy components
const HeavyComponent = dynamic(() => import('../components/HeavyComponent'), {
  ssr: false,
  loading: () => <div>Loading...</div>,
});

export default function PerformanceOptimizedPage() {
  const [data, setData] = useState(null);

  // Code splitting: Load data only when needed
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('/api/data');
      const data = await response.json();
      setData(data);
    };

    fetchData();
  }, []);

  // Server-side rendering: Pre-render data
  export async function getServerSideProps() {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();

    return {
      props: {
        data,
      },
    };
  }

  // Static site generation: Pre-render at build time
  export async function getStaticProps() {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();

    return {
      props: {
        data,
      },
      revalidate: 60, // In seconds
    };
  }

  return (
    <div>
      <h1>Performance Optimized Page</h1>
      {data && <HeavyComponent data={data} />}
    </div>
  );
}
```