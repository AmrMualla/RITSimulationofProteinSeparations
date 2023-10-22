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
            <div className="content">
                {/* Content goes here */}
                <div className="simulation">{Router()}</div>
            </div>
        </div>
    );
}

export default App;
