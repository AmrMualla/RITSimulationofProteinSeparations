import React from 'react';
import { render, fireEvent, screen, act } from '@testing-library/react';
import OneDE from '../OneDE';
import startAnimation from '../OneDE';

describe('OneDE', () => {
  test('labels render correctly', () => {
    render(<OneDE />);

    // Check if the initial state is rendered correctly
    expect(screen.getByText('Voltage:')).toBeInTheDocument();
    expect(screen.getByText('Current Wells: 10')).toBeInTheDocument();
    expect(screen.getByText('Acrylamide %:')).toBeInTheDocument();

    // Check if the file and folder buttons are rendered
    expect(screen.getByText('File')).toBeInTheDocument();
    expect(screen.getByText('Folder')).toBeInTheDocument();

    // Check if the "Add Well" and "Drop Well" buttons are rendered
    expect(screen.getByText('Add Well')).toBeInTheDocument();
    expect(screen.getByText('Drop Well')).toBeInTheDocument();

  });

  test('Voltage dropdown works correctly', () => {
    render(<OneDE />);

    // Verify that the dropdown is rendered
    const dropdown = screen.getByTestId('voltage-dropdown');
    expect(dropdown).toBeInTheDocument();

    // Verify that each option is rendered
    const options = ['50V-option', '100V-option', '150V-option', '200V-option'];
    options.forEach((option) => {
      const dropdownOption = screen.getByTestId(option);
      expect(dropdownOption).toBeInTheDocument();
    });

    // Simulate a change event and verify that the value is updated
    fireEvent.change(dropdown, { target: { value: '100V' } });
    expect(dropdown.value).toBe('100V');
  });

  test('Acrylamide dropdown works correctly', () => {
    render(<OneDE />);

    // Verify that the dropdown is rendered
    const dropdown = screen.getByTestId('acrylamide-dropdown');
    expect(dropdown).toBeInTheDocument();

    // Verify that each option is rendered
    const options = ['7.5%-option', '10%-option', '15%-option'];
    options.forEach((option) => {
      const dropdownOption = screen.getByTestId(option);
      expect(dropdownOption).toBeInTheDocument();
    });

    // Simulate a change event and verify that the value is updated
    fireEvent.change(dropdown, { target: { value: '10%' } });
    expect(dropdown.value).toBe('10%');
  });

  test('handles well count changes correctly', () => {
    render(<OneDE />);

    // Check if the initial well count is correct
    expect(screen.getByText('Current Wells: 10')).toBeInTheDocument();
    var numOfWells = screen.getAllByTestId('wells#');
    expect(numOfWells.length).toBe(10);

    // Click on "Add Well" button
    fireEvent.click(screen.getByText('Add Well'));

    // Check if the well count is updated
    expect(screen.getByText('Current Wells: 11')).toBeInTheDocument();
    numOfWells = screen.getAllByTestId('wells#');
    expect(numOfWells.length).toBe(11);

    // Click on "Drop Well" button
    fireEvent.click(screen.getByText('Drop Well'));

    // Check if the well count is updated
    expect(screen.getByText('Current Wells: 10')).toBeInTheDocument();
    numOfWells = screen.getAllByTestId('wells#');
    expect(numOfWells.length).toBe(10);
  });
});
