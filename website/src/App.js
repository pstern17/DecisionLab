import logo from './logo.svg';
import './App.css';
import HostPage from './components/HostPage.js';
import HomePage from './components/HomePage.js';
import Navbar from './components/Navbar.js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar></Navbar>
        <HomePage></HomePage>
        <HostPage></HostPage>
      </header>
    </div>
  );
}

export default App;
