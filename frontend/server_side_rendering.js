```javascript
import { GetServerSideProps } from 'next';
import fetch from 'isomorphic-unfetch';

export const getServerSideProps: GetServerSideProps = async context => {
  const res = await fetch(`http://localhost:3000/api/data`);
  const data = await res.json();

  if (!data) {
    return {
      notFound: true,
    }
  }

  return {
    props: { data }, // will be passed to the page component as props
  }
}

const ServerSideRenderingPage = ({ data }) => {
  return (
    <div id="ai-output">
      {data.map((item, index) => (
        <div key={index}>
          <h2>{item.title}</h2>
          <p>{item.content}</p>
        </div>
      ))}
    </div>
  );
}

export default ServerSideRenderingPage;
```