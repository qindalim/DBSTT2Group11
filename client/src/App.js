import "bootstrap/dist/css/bootstrap.min.css";
import './App.css';
import { Link, BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import NewClaim from './componets/newClaim'
import Login from './componets/login'
import Home from "./componets/home"
import NavRouter from "./navRouter"


function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand navbar-dark bg-dark">
          <li className="nav-item">
            <a href='http://localhost:3000/'>Login</a>
          </li>
          <li className="nav-item">
            <a href='http://localhost:3000/home'>Home</a>
          </li>
          <li className="nav-item">
            <a href='http://localhost:3000/newclaim'>Add claim</a>
          </li>
      </nav>
      <NavRouter/>

		</div>
	);
}

export default App;