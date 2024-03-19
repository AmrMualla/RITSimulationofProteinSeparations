import React, { useState } from 'react';
import { useLocalStorage } from 'usehooks-ts'
import * as ReactDOM from "react-dom/client";
import Sidebar from './components/Sidebar.js';
import Router from './Router.js';
import './App.css';


function App() {
    const [isSidebarOpen, setIsSidebarOpen] = useLocalStorage('isSidebarOpen', true);

    return (
        <div className="app-container">
            <Sidebar isOpen={isSidebarOpen} toggle={() => setIsSidebarOpen(!isSidebarOpen)} />
            <Router isOpen={isSidebarOpen} />
        </div>
    );
}

// Function to toggle dark mode
function toggleDarkMode() {
    const body = document.body;
    if (document.querySelector('.options-box') != null) {
        const optionsBox = document.querySelector('.options-box');
        optionsBox.classList.toggle('dark-mode');
    }
    //const optionsBox = document.querySelector('.options-box');
    const sidebar = document.querySelector('.sidebar');
    const sidebarHeader = document.querySelector('.sidebar-header');
    
    body.classList.toggle('dark-mode');
    
    sidebar.classList.toggle('dark-mode');
    sidebarHeader.classList.toggle('dark-mode');

    // Save the user's preference to localStorage
    const isDarkMode = body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}

// Check if the user has a dark mode preference
const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
const storedDarkMode = JSON.parse(localStorage.getItem('darkMode'));
if (storedDarkMode !== null) {
    document.body.classList.toggle('dark-mode', storedDarkMode);
} else {
    document.body.classList.toggle('dark-mode', prefersDarkMode);
}

// Add event listener to the dark mode toggle button
const darkModeToggle = document.getElementById('dark-mode-toggle');
darkModeToggle.addEventListener('click', toggleDarkMode);

export default App;
