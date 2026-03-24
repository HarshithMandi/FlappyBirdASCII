import { useState } from 'react';


const LoginForm = () => {
    const[username, setUsername] = useState('');
    const[password, setPassword] = useState('');
    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Username: ${username}, Password: ${password}`);
        setUsername('');
        setPassword('');
    };
    return (
        <div>
            <h1>Login Form</h1>
            <p>This is the LoginForm page.</p>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username:</label>
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} /><br />
                </div>
                <div>
                    <label>Password:</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} /><br />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default LoginForm;
