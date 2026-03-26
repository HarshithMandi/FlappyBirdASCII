
import { screen, render, fireEvent } from '@testing-library/react';
import { describe, test, expect } from 'vitest';
import { MemoryRouter } from 'react-router-dom';
import LoginForm from './LoginForm';

describe('LoginForm',() => {
    test('renders username and password fields', () => {
        render(
            <MemoryRouter>
                <LoginForm />
            </MemoryRouter>
        );
        expect(screen.getByLabelText(/username/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/password/i)).toBeInTheDocument();

    })

    test('Updates username input value', () => {
        render(
            <MemoryRouter>
                <LoginForm />
            </MemoryRouter>
        );
        const usernameInput = screen.getByLabelText(/username/i);
        fireEvent.change(usernameInput, {target:{value:'testuser'}});
        expect(usernameInput.value).toBe('testuser');
    })
})
