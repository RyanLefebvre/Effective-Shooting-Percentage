import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import MainInfoComp from './components/MainInfoComp';
import NavBarComp from './components/NavBarComp';

function App() {
  return (
    <div className="App">
      <NavBarComp />
      <MainInfoComp />
    </div>
  );
}

export default App;
