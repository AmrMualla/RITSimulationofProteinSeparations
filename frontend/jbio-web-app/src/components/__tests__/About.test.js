import React from 'react';
import { getAllByText, render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect'; // For the "toBeInTheDocument" matcher
import About from '../About';

test('renders About component content', () => {
  const { getByText, getByTestId, getByAltText } = render(<About />);

  // Check if the component renders the correct headers and content
  expect(getByText('About')).toBeInTheDocument();
  expect(getByTestId('projPurpose-header')).toBeInTheDocument();
  expect(getByTestId('commUse-header')).toBeInTheDocument();
  expect(getByTestId('projOwner-header')).toBeInTheDocument();
  expect(getByTestId('currDevs-header')).toBeInTheDocument();
  expect(getByTestId('historicDevs-header')).toBeInTheDocument();
  
  // Check if images are rendered with alt text
  expect(getByAltText('Paul Craig-pic')).toBeInTheDocument();
  expect(getByAltText('Chase Amador-pic')).toBeInTheDocument();
  expect(getByAltText('Beck Anderson-pic')).toBeInTheDocument();
  expect(getByAltText('Landon Heatly-pic')).toBeInTheDocument();
  expect(getByAltText('Mack Leonard-pic')).toBeInTheDocument();
  expect(getByAltText('Amr Mualla-pic')).toBeInTheDocument();

});

test('renders About component Navbar', () => {
  const { getByText, getByTestId, getByAltText } = render(<About />);

  // Check if the component renders the correct navbar elements
  expect(getByTestId('projPurpose-nav')).toBeInTheDocument();
  expect(getByTestId('commUse-nav')).toBeInTheDocument();
  expect(getByTestId('projOwner-nav')).toBeInTheDocument();
  expect(getByTestId('currDevs-nav')).toBeInTheDocument();
  expect(getByTestId('historicDevs-nav')).toBeInTheDocument();

});