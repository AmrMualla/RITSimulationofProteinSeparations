import React, { useState } from 'react';
import { useLocalStorage } from 'usehooks-ts'
import * as ReactDOM from "react-dom/client";
import Sidebar from './components/Sidebar.js';
import Router from './Router.js';
import { DarkToggle } from './components/DarkToggle.js';
import './App.css';


function App() {
    const [isSidebarOpen, setIsSidebarOpen] = useLocalStorage('isSidebarOpen', true);
    const preference = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const [isDark, setIsDark] = useLocalStorage('isDark', preference);

    return (
        <div className="app-container" data-theme={isDark ? "dark" : "light"}>
            <Sidebar isOpen={isSidebarOpen} isDark={isDark} toggle={() => setIsSidebarOpen(!isSidebarOpen)} />
            <Router isOpen={isSidebarOpen} />
            <DarkToggle isChecked={isDark} handleChange={() => setIsDark(!isDark)} />
        </div>
    );
}

export default App;
