import React, { useState } from 'react';
import App from '../App';
import '../components/Sidebar.css';

function Sidebar({ isOpen, toggle, isDark }) {
    const [isHoveredGithub, setHoveredGithub] = useState(false);
    const [isHoveredInfo, setHoveredInfo] = useState(false);
    const [isHoveredUser, setHoveredUser] = useState(false);
    const [isHoveredAbout, setHoveredAbout] = useState(false);
    
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
                        <a href="/">
                            <span>
                                <img
                                    src={isHoveredAbout ? "/information-button-hover.png" : "/information-button.png"}
                                    alt="Information"
                                    className="about-icon"
                                    data-testId = 'about-icon'
                                    onMouseEnter={() => setHoveredAbout(true)}
                                    onMouseLeave={() => setHoveredAbout(false)}
                                />
                            </span>
                        </a>
                        <a href="1de"><span className="hoverable-text" data-testId = '1de-icon'>1DE</span></a>
                        <a href="2de"><span className="hoverable-text" data-testId = '2de-icon'>2DE</span></a>

                        {/* Fill in icon here^^^ */}

                        <a href="instructions">
                            <span>
                                <img
                                    src={isHoveredInfo ? "/list-hover.png" : "/list.png"}
                                    alt="Information"
                                    className="instructions-icon"
                                    data-testId = 'instructions-icon'
                                    onMouseEnter={() => setHoveredInfo(true)}
                                    onMouseLeave={() => setHoveredInfo(false)}
                                />
                            </span>
                        </a>

                        <a href="contact">
                            <span>
                                <img
                                    src={isHoveredUser ? "/user-hover.png" : "/user.png"}
                                    alt="User"
                                    className="contact-icon"
                                    data-testId = 'contact-icon'
                                    onMouseEnter={() => setHoveredUser(true)}
                                    onMouseLeave={() => setHoveredUser(false)}
                                />
                            </span>
                        </a>

                        <a href="https://github.com/AmrMualla/RITSimulationofProteinSimulations" target="_blank" rel="noopener noreferrer">
                            <span>
                                <img
                                    src={isHoveredGithub ? "/github-sign-hover.png" : "/github-sign.png"}
                                    alt="Github"
                                    className="github-icon"
                                    data-testId = 'github-icon'
                                    onMouseEnter={() => setHoveredGithub(true)}
                                    onMouseLeave={() => setHoveredGithub(false)}
                                />
                            </span>
                        </a>
                    </div>
                )}

                { isOpen && (
                    <ul className="menu">
                        <a href="/"><li className="hoverable-text" data-testId = 'about-text'>About</li></a>
                        <a href="1de"><li className="hoverable-text" data-testId = '1de-text'>1D Electrophoresis</li></a>
                        <a href="2de"><li className="hoverable-text" data-testId = '2de-text'>2D Electrophoresis</li></a>

                        {/* Fill in name here^^^ */}
                        <a href="instructions"><li className="hoverable-text" data-testId = 'instructions-text'>Instructions</li></a>
                        <a href="contact"><li className="hoverable-text" data-testId = 'contact-text'>Contact</li></a>
                        <a href="https://github.com/AmrMualla/RITSimulationofProteinSimulations" target="_blank" rel="noopener noreferrer"><li className="hoverable-text" data-testId = 'github-text'>Github</li></a>
                    </ul>
                )}
            </div>
            <div className="sidebar-header">
                <a href="/">
                    <span>
                        <img 
                            id="basil-logo" 
                            src={isDark ? "/basil-logo-darkmode.png" : "/basil-logo.png"} 
                            alt="Basil"
                        />
                    </span>
                </a>
            </div>
        </div>
    );
}

export default Sidebar;
