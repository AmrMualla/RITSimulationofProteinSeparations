import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect'; // For the "toBeInTheDocument" matcher
import Contact from '../Contact';

test('renders Contact component', () => {
  const { getByText, getByRole } = render(<Contact />);

  // Check if the component renders the correct header and content
  expect(getByText('Contact')).toBeInTheDocument();
  expect(getByText('Team Members')).toBeInTheDocument();
  expect(getByText('Amr Mualla')).toBeInTheDocument();
  expect(getByText('Email: am3576@rit.edu')).toBeInTheDocument();
  expect(getByText('Phone: (347) 631-7359')).toBeInTheDocument();
  expect(getByText('Beck Anderson')).toBeInTheDocument();
  expect(getByText('Email: bea1935@rit.edu')).toBeInTheDocument();
  expect(getByText('Phone: (716) 640-2894')).toBeInTheDocument();
  expect(getByText('Chase Amador')).toBeInTheDocument();
  expect(getByText('Email: cma6320@rit.edu')).toBeInTheDocument();
  expect(getByText('Phone: (203) 725-4442')).toBeInTheDocument();
  expect(getByText('Landon Heatly')).toBeInTheDocument();
  expect(getByText('Email: lbh1442@rit.edu')).toBeInTheDocument();
  expect(getByText('Phone: (203) 832-9841')).toBeInTheDocument();
  expect(getByText('Mack Leonard')).toBeInTheDocument();
  expect(getByText('Email: mml2034@rit.edu')).toBeInTheDocument();
  expect(getByText('Phone: (203) 731-9620')).toBeInTheDocument();

  expect(getByText('Team Coach')).toBeInTheDocument();
  expect(getByText('Mark Wilson')).toBeInTheDocument();
  expect(getByText('RIT Email: mwvse@rit.edu')).toBeInTheDocument();
  expect(getByText('Personal Email: mwilson1962@gmail.com')).toBeInTheDocument();

  expect(getByText('Project Sponsor')).toBeInTheDocument();
  expect(getByText('Dr. Paul Craig')).toBeInTheDocument();
  expect(getByText('Email: pac8612@rit.edu')).toBeInTheDocument();
  expect(getByText('Office Phone: (585) 475-6145')).toBeInTheDocument();

});