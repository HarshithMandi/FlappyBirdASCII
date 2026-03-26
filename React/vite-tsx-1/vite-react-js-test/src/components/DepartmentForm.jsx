
import {useState} from 'react'

const DepartmentForm = () => {
    const [DepartmentName, setDepartmentName] = useState('')
  return (
    <div>
    <h1>Department Form</h1>
    <form>
        <label htmlFor='deptname'> Department Name: </label>
        <select id='deptname' value={DepartmentName} onChange={(e) => setDepartmentName(e.target.value)}>
            <option value=''> Select Department</option>
            <option value='HR'> HR </option>
            <option value='IT'> IT </option>
            <option value='Finance'> Finance </option>
        </select>
        <p> Selected Department: {DepartmentName}</p>
    </form>
    </div>
  )
}

export default DepartmentForm