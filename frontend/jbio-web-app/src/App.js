import React, { useState } from 'react';
import Sidebar from './components/Sidebar.js';
import './App.css';


function App() {
    const [isSidebarOpen, setIsSidebarOpen] = useState(true);

    return (
        <div className="app-container">
            <Sidebar isOpen={isSidebarOpen} toggle={() => setIsSidebarOpen(!isSidebarOpen)} />
            <div className="content">
                {/* Content goes here */}
                <div className="simulation"></div>
            </div>
        </div>
    );
}

export default App;
