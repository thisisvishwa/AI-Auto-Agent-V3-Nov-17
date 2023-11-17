```javascript
import { GetStaticProps } from 'next';
import { fetchData } from './data_fetching.js';
import { manageState } from './state_management.js';

export const getStaticProps: GetStaticProps = async () => {
  const data = await fetchData();
  return {
    props: {
      data,
    },
    revalidate: 1, // In seconds
  };
};

const StaticSite = ({ data }) => {
  const state = manageState(data);

  return (
    <div>
      {state.map((item, index) => (
        <div key={index}>
          <h2>{item.title}</h2>
          <p>{item.description}</p>
        </div>
      ))}
    </div>
  );
};

export default StaticSite;
```