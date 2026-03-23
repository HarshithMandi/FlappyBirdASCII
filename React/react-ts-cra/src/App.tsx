import './App.css';

import { useState } from 'react';

type CounterProps = {
  initial: number;
};

function Counter({ initial }: CounterProps) {
  const [count, setCount] = useState<number>(initial);

  return (
    <button type="button" onClick={() => setCount((c) => c + 1)}>
      Count: {count}
    </button>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>React + TypeScript</h1>
        <p>Lesson 1: typed props + typed state</p>
        <Counter initial={0} />
      </header>
    </div>
  );
}

export default App;
