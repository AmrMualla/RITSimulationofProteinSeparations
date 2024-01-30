import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Sidebar from '../Sidebar';

// TODO
/*
describe('Sidebar', () => {
  test('renders correctly', () => {
    // Mock toggle function
    const mockToggle = jest.fn();

    // Render the Sidebar component
    const { getByRole, getByAltText, getByText } = render(
      <Sidebar isOpen={false} toggle={mockToggle} />
    );

    // Check if the toggle button is rendered
    expect(getByRole('button', { className: /toggle-btn/i })).toBeInTheDocument();

    // Check if the Basil logo is rendered
    expect(getByAltText('Basil')).toBeInTheDocument();

    // TODO
    // Check if some links are rendered when the sidebar is not open
    //expect(getByText('About')).toBeInTheDocument();
    //expect(getByText('1D Electrophoresis')).toBeInTheDocument();
    //expect(getByText('2D Electrophoresis')).toBeInTheDocument();

    // Click the toggle button to open the sidebar
    fireEvent.click(getByRole('button', { className: /toggle-btn/i }));

    // Check if the links are rendered when the sidebar is open
    expect(getByText('Instructions')).toBeInTheDocument();
    expect(getByText('Contact')).toBeInTheDocument();
    expect(getByText('Github')).toBeInTheDocument();

    // Optionally, you can check if the toggle function is called when the button is clicked
    fireEvent.click(getByRole('button', { className: /toggle-btn/i }));
    expect(mockToggle).toHaveBeenCalled();
  });
}); */

test('renders open Sidebar components', () => {
  const mockToggle = jest.fn();

  // Render the Sidebar component
  const { getByTestId } = render(<Sidebar isOpen={true} toggle={mockToggle} />);

  expect(getByTestId('about-text')).toBeInTheDocument();
  expect(getByTestId('1de-text')).toBeInTheDocument();
  expect(getByTestId('2de-text')).toBeInTheDocument();
  expect(getByTestId('instructions-text')).toBeInTheDocument();
  expect(getByTestId('contact-text')).toBeInTheDocument();
  expect(getByTestId('github-text')).toBeInTheDocument();

});

test('renders closed Sidebar components', () => {
  const mockToggle = jest.fn();

  // Render the Sidebar component
  const { getByTestId } = render(<Sidebar isOpen={false} toggle={mockToggle} />);

  expect(getByTestId('about-icon')).toBeInTheDocument();
  expect(getByTestId('1de-icon')).toBeInTheDocument();
  expect(getByTestId('2de-icon')).toBeInTheDocument();
  expect(getByTestId('instructions-icon')).toBeInTheDocument();
  expect(getByTestId('contact-icon')).toBeInTheDocument();
  expect(getByTestId('github-icon')).toBeInTheDocument();
});