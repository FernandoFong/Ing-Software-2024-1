import { useState } from 'react';
import './App.css';
import Name from './Name';
import NewNameForm from './NewNameForm';

function App() {

  const [name, setName] = useState({
    name:undefined,
    last_name:undefined
  });

  function fetchNameHandler() {
    fetch('http://127.0.0.1:5000/simulator')
    .then((response) => {
      return response.json(); //Si aquí hay un error, quiere decir que el back-end está mal.
    })
    .then((data) => { //Lambda en JS
      setName(data);
    })
  }

  async function addName (name) {
    console.log(name);
    const response = await fetch('http://127.0.0.1:5000/add_name', {
      method:'POST',
      body: JSON.stringify(name),
      headers: {
        'Content-Type':'application/json'
      }
    });
    const data = await response.json();
    console.log(data);
    if (data.error !== undefined) {
      alert("ERROR! " + data.error);
    } else {
      alert("Name added!");
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <Name name={name} />
        <button onClick={fetchNameHandler}>New Name</button>
        <NewNameForm onSaveName={addName}/>
      </header>
    </div>
  );
}

export default App;
