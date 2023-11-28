import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect'; // For the "toBeInTheDocument" matcher
import Instructions from '../Instructions';

test('renders Instructions component', () => {
  const { getByText, getByRole, getByAltText } = render(<Instructions />);

  // Check if the component renders the correct headers
  expect(getByText('Instructions')).toBeInTheDocument();
  expect(getByText('One-Dimensional Gel Electrophoresis')).toBeInTheDocument();
  expect(getByText('Two-Dimensional Gel Electrophoresis')).toBeInTheDocument();
  expect(getByText('Three-Dimensional Gel Electrophoresis')).toBeInTheDocument();

  // Check if the component renders the correct content
  expect(getByText('Select the number of wells')).toBeInTheDocument();
  expect(getByText('Select the proteins you want to test')).toBeInTheDocument();
  expect(getByText('Select an Acrylamide percentage')).toBeInTheDocument();
  expect(getByText('Select the standards you want present')).toBeInTheDocument();
  expect(getByText('Select a voltage')).toBeInTheDocument();
  expect(getByText('Press the Add Sample button')).toBeInTheDocument();
  expect(getByText('Press the Start Run button')).toBeInTheDocument();

  // Check if the component renders the image with alt text
  expect(getByAltText('3de')).toBeInTheDocument();
});
