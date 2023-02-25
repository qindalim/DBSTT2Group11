import { Link, BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import NewClaim from './componets/newClaim'
import Login from './componets/login'
import Home from "./componets/home"
 
import './App.css';

function NavRouter() {
  return (
   <Router>
        <Routes> 
            <Route path='/' element={<Login/>}  />
            <Route path='/newclaim' element={<NewClaim/>} />
            <Route path='/home' element={<Home/>} />
        </Routes>
    </Router>
	);
}

export default NavRouter;