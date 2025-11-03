import { render, screen, fireEvent } from '@testing-library/react';
import Login from '../Login';
import { MemoryRouter } from 'react-router-dom';

test('renders login form', () => {
  render(<MemoryRouter><Login/></MemoryRouter>);
  expect(screen.getByPlaceholderText(/email/i)).toBeInTheDocument();
  expect(screen.getByPlaceholderText(/password/i)).toBeInTheDocument();
});
