import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import OneDE from '../OneDE';

describe('OneDE', () => {
  test('renders correctly', () => {
    render(<OneDE />);

    // Check if the initial state is rendered correctly
    expect(screen.getByText('Voltage:')).toBeInTheDocument();
    expect(screen.getByText('Current Wells: 5')).toBeInTheDocument();
    expect(screen.getByText('Acrylamide: 7.5%')).toBeInTheDocument();

    // Check if the file and folder buttons are rendered
    expect(screen.getByText('File')).toBeInTheDocument();
    expect(screen.getByText('Folder')).toBeInTheDocument();

    //TODO
    // Check if the voltage dropdown is rendered
    /*expect(screen.getByLabelText('Voltage:')).toBeInTheDocument();
    expect(screen.getByText('50V')).toBeInTheDocument();
    expect(screen.getByText('100V')).toBeInTheDocument();
    expect(screen.getByText('150V')).toBeInTheDocument();
    expect(screen.getByText('200V')).toBeInTheDocument();*/

    // Check if the "Add Well" and "Drop Well" buttons are rendered
    expect(screen.getByText('Add Well')).toBeInTheDocument();
    expect(screen.getByText('Drop Well')).toBeInTheDocument();

    // Check if the wells are rendered based on the initial well count
    //expect(screen.getAllByTestId('well').length).toBe(5);

    // Check if the acrylamide dropdown is rendered
    /*expect(screen.getByLabelText('Acrylamide %:')).toBeInTheDocument();
    expect(screen.getByText('7.5%')).toBeInTheDocument();
    expect(screen.getByText('10%')).toBeInTheDocument();
    expect(screen.getByText('15%')).toBeInTheDocument();*/
  });

  test('handles well count changes correctly', () => {
    render(<OneDE />);

    // Check if the initial well count is correct
    expect(screen.getByText('Current Wells: 5')).toBeInTheDocument();

    // Click on "Add Well" button
    fireEvent.click(screen.getByText('Add Well'));

    // Check if the well count is updated
    expect(screen.getByText('Current Wells: 6')).toBeInTheDocument();

    // Click on "Drop Well" button
    fireEvent.click(screen.getByText('Drop Well'));

    // Check if the well count is updated
    expect(screen.getByText('Current Wells: 5')).toBeInTheDocument();
  });
});
