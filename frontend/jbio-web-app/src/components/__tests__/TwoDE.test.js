import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect'; // For the "toBeInTheDocument" matcher
import TwoDE from '../TwoDE';

test('renders TwoDE component', () => {
  const { getByText, getByRole } = render(<TwoDE />);

  // Check if the component renders the correct header
  expect(getByText('2DE page')).toBeInTheDocument();
  
});