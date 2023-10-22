import React, { useState } from 'react';
import * as ReactDOM from "react-dom/client";
import Sidebar from './components/Sidebar.js';
import Router from './Router.js';
import './App.css';


function App() {
    const [isSidebarOpen, setIsSidebarOpen] = useState(true);

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
