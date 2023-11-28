import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect'; // For the "toBeInTheDocument" matcher
import About from '../About';

test('renders About component', () => {
  const { getByText, getByTestId, getByAltText } = render(<About />);

  // TODO
  // Check if the component renders the correct headers and content
  expect(getByText('About')).toBeInTheDocument();
  expect(getByText('Project Purpose')).toBeInTheDocument();
  expect(getByText('JBioFramework (JBF) is a set of chemical simulations frequently used in chemistry,')).toBeInTheDocument();
  expect(getByText('Commercial Use')).toBeInTheDocument();
  expect(getByText('Project Owner')).toBeInTheDocument();
  expect(getByText('Current Developers')).toBeInTheDocument();
  expect(getByText('Historic Developers')).toBeInTheDocument();
  
  // Check if images are rendered with alt text
  expect(getByAltText('profile-icon')).toBeInTheDocument();
  expect(getByAltText('Paul Craig')).toBeInTheDocument();
  expect(getByAltText('Chase Amador')).toBeInTheDocument();
  expect(getByAltText('Beck Anderson')).toBeInTheDocument();
  expect(getByAltText('Landon Heatly')).toBeInTheDocument();
  expect(getByAltText('Mack Leonard')).toBeInTheDocument();
  expect(getByAltText('Amr Mualla')).toBeInTheDocument();
  expect(getByAltText('Place Holder')).toBeInTheDocument();

});