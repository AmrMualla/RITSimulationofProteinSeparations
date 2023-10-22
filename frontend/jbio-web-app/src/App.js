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

export default App;
