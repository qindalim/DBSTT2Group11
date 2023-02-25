import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import NewClaim from './componets/newClaim'
import Login from './componets/login'
import Home from "./componets/home"


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Router>
          <Routes> 
            <Route path='/' element={<Login/>} />
            <Route path='/newclaim' element={<NewClaim/>} />
            <Route path='/home' element={<Home/>} />
          </Routes>
        </Router>
      </header>
		</div>
	);
}

export default App;