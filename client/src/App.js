<<<<<<< Updated upstream
import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import NewClaim from './componets/newClaim'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Router>
          <Routes>
            <Route path='/newclaim' element={<NewClaim/>} />
          </Routes>
        </Router>
        
=======
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import Home from "./componets/home";


function App() {
	return (
		<div className = "App">
      <header className = "App-header">
        <Router> 
          <Routes>
            <Route path='/home' element={<Home/>} />
          </Routes>
        </Router>
>>>>>>> Stashed changes
      </header>
		</div>
	);
}

export default App;