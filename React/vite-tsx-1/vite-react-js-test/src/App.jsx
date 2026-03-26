

import './App.css'
import {Routes, Route, Link} from 'react-router-dom'
import Home from './components/Home'
import Contact from './components/Contact'
import About from './components/About'
import NotFound from './components/NotFound'
import LoginForm from './components/LoginForm'
import DepartmentForm from './components/DepartmentForm'
import SkillForm from './components/SkillForm'
import AddProduct from './components/addProduct'
import ProductList from './components/ProductList'

function App() {
  return (
    <>
    <nav>
      <ul>
        <li> <Link to='/'>Home</Link></li>
        <li> <Link to='/contact'>Conact Us</Link></li>
        <li> <Link to='/login'>Login</Link></li>
        <li> <Link to ='/skills'>Skill Form</Link></li>
        <li> <Link to='/department'>Department Form</Link></li>
        <li> <Link to='/product'>Product List</Link></li>
        <li> <Link to='/add_product'> Add Product </Link></li>
      </ul>
    </nav>
    <Routes>
      <Route path = '/' element = {<Home />} />
      <Route path='/contact' element = {<Contact />} />
      <Route path='/login' element = {<LoginForm />} />
      <Route path = '/about' element = {<About />} />
      <Route path = '/department' element = {<DepartmentForm />} />
      <Route path='/skills' element = {<SkillForm />} />
      <Route path ='*' element = {<NotFound />} />
      <Route path='/product' element = {<ProductList />} />
      <Route path ='/add_product' element = {<AddProduct />} />
    </Routes>
    </>
  )
}

export default App