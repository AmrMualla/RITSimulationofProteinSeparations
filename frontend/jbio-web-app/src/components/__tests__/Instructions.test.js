import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect'; // For the "toBeInTheDocument" matcher
import Instructions from '../Instructions';

test('renders Instructions component content', () => {
  const { getByText, getByTestId, getByAltText } = render(<Instructions />);

  // Check if the component renders the correct headers
  expect(getByText('Instructions')).toBeInTheDocument();
  expect(getByTestId('1de-header')).toBeInTheDocument();
  expect(getByTestId('2de-header')).toBeInTheDocument();
  expect(getByTestId('3de-header')).toBeInTheDocument();

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

test('renders Instructions component navbar', () => {
  const { getByTestId } = render(<Instructions />);

  // Check if the component renders the correct navbar elements
  expect(getByTestId('1de-nav')).toBeInTheDocument();
  expect(getByTestId('2de-nav')).toBeInTheDocument();
  expect(getByTestId('3de-nav')).toBeInTheDocument();
});