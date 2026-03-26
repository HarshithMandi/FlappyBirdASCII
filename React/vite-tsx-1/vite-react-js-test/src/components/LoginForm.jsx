import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

const LoginForm = () => {
    const navigate = useNavigate()
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const handleSubmit = (e) => {
        e.preventDefault()
        alert(`Username: ${username}, Password: ${password}`)
        setUsername('')
        setPassword('')
        navigate('/')
    }

    return (
        <div>
            <form onSubmit = {handleSubmit}>
                <div>
                    <h1>Login</h1>
                    <label>Username:</label>
                    <input type='text' value={username} onChange={(e) => setUsername(e.target.value)} /><br />
                    <label>Password:</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                    <button type ='submit'>Log in</button>
                </div>
            </form>
        </div>
    )
}

export default LoginForm
