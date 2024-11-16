import React, { useState } from 'react';

function App() {
  const [status, setStatus] = useState('');

  const handleRunScript = async () => {
    try {
      const result = await window.electron.runPythonScript();
      setStatus(result); // Display success message
    } catch (error) {
      setStatus(`Error: ${error}`);
    }
  };

  return (
    <div>
      <h1>Multiverse App</h1>
      <button onClick={handleRunScript}>Run Python Script</button>
      <p>{status}</p>
    </div>
  );
}

export default App;