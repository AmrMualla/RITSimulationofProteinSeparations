import React, { useState } from 'react';

function Sidebar({ isOpen, toggle }) {
    const [isHoveredGithub, setHoveredGithub] = useState(false);
    const [isHoveredInfo, setHoveredInfo] = useState(false);
    const [isHoveredUser, setHoveredUser] = useState(false);
    
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
                        <span className="hoverable-text"><a href="/">a</a></span>
                        <span className="hoverable-text"><a href="1de">1DE</a></span>
                        <span className="hoverable-text"><a href="2de">2DE</a></span>
                        
                        <a href="instructions">
                            <img
                                src={isHoveredInfo ? "/information-button-hover.png" : "/information-button.png"}
                                alt="Information"
                                className="instructions-icon"
                                onMouseEnter={() => setHoveredInfo(true)}
                                onMouseLeave={() => setHoveredInfo(false)}
                            />
                        </a>

                        <a href="contact">
                            <img
                                src={isHoveredUser ? "/user-hover.png" : "/user.png"}
                                alt="User"
                                className="contact-icon"
                                onMouseEnter={() => setHoveredUser(true)}
                                onMouseLeave={() => setHoveredUser(false)}
                            />
                        </a>

                        <a href="https://github.com/AmrMualla/RITSimulationofProteinSimulations" target="_blank" rel="noopener noreferrer">
                            <img 
                                src={isHoveredGithub ? "/github-sign-hover.png" : "/github-sign.png"} 
                                alt="Github" 
                                className="github-icon"
                                onMouseEnter={() => setHoveredGithub(true)}
                                onMouseLeave={() => setHoveredGithub(false)}
                            />
                        </a>
                    </div>
                )}

                { isOpen && (
                    <ul className="menu">
                        <li className="hoverable-text"><a href="/">About</a></li>
                        <li className="hoverable-text"><a href="1de">1D Electrophoresis</a></li>
                        <li className="hoverable-text"><a href="2de">2D Electrophoresis</a></li>
                        <li className="hoverable-text"><a href="instructions">Instructions</a></li>
                        <li className="hoverable-text"><a href="contact">Contact</a></li>
                        <li className="hoverable-text"><a href="https://github.com/AmrMualla/RITSimulationofProteinSimulations" target="_blank" rel="noopener noreferrer">Github</a></li>
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
