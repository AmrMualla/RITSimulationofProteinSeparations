import React from 'react';

function Sidebar({ isOpen, toggle }) {
    return (
        <div className="container">
            <div className={isOpen ? "sidebar" : "sidebar sidebar-collapsed"}>
                <button className="toggle-btn" onClick={toggle}>
                    <span></span>
                    <span></span>
                    <span></span>
                </button>

                { !isOpen && (
                    <div className="icon-list">
                        <span>1DE</span>
                        <span>2DE</span>
                        <img src="information-button.png" alt="" className="instructions-icon" />
                        <img src="user.png" alt="" className="contact-icon" />
                        <a href="https://github.com/AmrMualla/RITSimulationofProteinSimulations" target="_blank" rel="noopener noreferrer">
                            <img src="github-sign.png" alt="" className="github-icon" />
                        </a>
                    </div>
                )}

                { isOpen && (
                    <ul className="menu">
                        <li>1D Electrophoresis</li>
                        <li>2D Electrophoresis</li>
                        <li>Instructions</li>
                        <li>Contact</li>
                        <li><a href="https://github.com/AmrMualla/RITSimulationofProteinSimulations" target="_blank" rel="noopener noreferrer">Github</a></li>
                    </ul>
                )}
            </div>
            <div className="sidebar-header">
                <span className="sidebar-title">JBioFramework</span>
            </div>
        </div>
    );
}

export default Sidebar;
