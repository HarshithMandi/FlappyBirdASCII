import './App.css'

import Home from './components/Home'
import About from './components/About'
import Contact from './components/Contact'
import NotFound from './components/notfound'
import LoginForm from './components/LoginForm'
import DepartmentForm from './components/Department'

import { Routes, Route, Link } from 'react-router-dom'

function App() {
  return(
    <div>
      <h1>My Website</h1>

      <nav style={{ display: 'flex', gap: 12, justifyContent: 'center' }}>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
        <Link to="/login">Login</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/department" element={<DepartmentForm />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  )
}

export default App
