import { useState } from 'react'

const DepartmentForm = () => {
    const [department, setDepartment] = useState('');
    return (
        <div>
            <h1>DepartmentForm</h1>
            <form>
                <label>Department:</label>
                <select value={department} onChange={(e) => setDepartment(e.target.value)}>
                    <option value="">Select a department</option>
                    <option value="HR">HR</option>
                    <option value="Engineering">Engineering</option>
                    <option value="Sales">Sales</option>
                </select><br />
                <p>Selected Department: {department}</p>
            </form>
        </div>
    );
};

export default DepartmentForm;