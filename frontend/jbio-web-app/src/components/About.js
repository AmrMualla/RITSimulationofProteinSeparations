import paul from './images/PaulPhoto.jpg';

function About() {
    return (
        <div>
            <div className="navbar">
                <a href="#project-purpose"><h2 className="section-header">Project Purpose</h2></a>
                <a href="#commercial-use"><h2 className="section-header">Commercial Use</h2></a>
                <a href="#project-owner"><h2 className="section-header">Project Owner</h2></a>
                <a href="#developers"><h2 className="section-header">Developers</h2></a>
            </div>
            <h1 className="page-header">About</h1>
            <h2 className="section-header" id="project-purpose">Project Purpose</h2>
            <p>
                JBioFramework (JBF) is a set of chemical simulations frequently used in chemistry,
                biochemistry, and proteomics research. It's main purpose is to allow for simplified simulation
                of proteins for academic and research opportunities. It is owned and operated by the RIT College of
                Science under the watch of Paul Craig. It is continuously being worked on with collaboration
                between the RIT College of Science and the RIT Software Engineering Department.
            </p>
            <h2 className="section-header" id="commercial-use">Commercial Use</h2>
                <ul>
                    <li>Students and teachers: Free</li>
                    <li>Under 50 audience members: Free</li>
                    <li>50-200 audience members: $100</li>
                    <li>Over 200 audience members: $500</li>
                    <li>Publish online: $100000000</li>
                </ul>
                <p>Piracy is not a victimless crime</p>
            <h2 className="section-header" id="project-owner">Project Owner</h2>
            <p>
                Lorem ipsum dolor sit amet
            </p>
            <div className="grid-container">
                <div className="grid-item">
                    <img src={paul} alt="profile-icon" style={{
                        borderRadius: "50%",
                        width: 200 + "px",
                        height: 200 + "px",
                        background: "red",
                        display: "grid",
                        justifyContent: "center"
                    }}/>
                    <figcaption style={{
                        fontSize: 20 + "px",
                        display: "grid",
                        justifyContent: "center"
                    }}>Paul Craig</figcaption>
                    <p style={{marginLeft: "auto"}}>
                        scelerisque et. Maecenas non nisi pellentesque, consectetur ante ac, dignissim massa. Phasellus
                        eleifend, augue at cursus scelerisque, est diam lacinia neque, nec laoreet neque mi a neque. Praesent
                        non bibendum risus. Nunc tristique massa eget mi venenatis, a sagittis mi imperdiet.
                    </p>
                </div>
            </div>
            <h2 className="section-header" id="developers">Developers</h2>
            <p>Lorem ipsum dolor sit amet</p>
            <div className="grid-container">
                <div className="grid-item">
                    <img src="https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-image-182145777.jpg" alt="profile-icon" style={{width:200 + "px"}} />
                    <figcaption style={{fontSize:20 + "px"}}>John Doe</figcaption>
                    <p>
                        scelerisque et. Maecenas non nisi pellentesque, consectetur ante ac, dignissim massa. Phasellus
                        eleifend, augue at cursus scelerisque, est diam lacinia neque, nec laoreet neque mi a neque. Praesent
                        non bibendum risus. Nunc tristique massa eget mi venenatis, a sagittis mi imperdiet.
                    </p>
                </div>
                <div className="grid-item">
                    <img src="https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-image-182145777.jpg" alt="profile-icon" style={{width:200 + "px"}} />
                    <figcaption style={{fontSize:20 + "px"}}>Also John Doe</figcaption>
                    <p>
                        scelerisque et. Maecenas non nisi pellentesque, consectetur ante ac, dignissim massa. Phasellus
                        eleifend, augue at cursus scelerisque, est diam lacinia neque, nec laoreet neque mi a neque. Praesent
                        non bibendum risus. Nunc tristique massa eget mi venenatis, a sagittis mi imperdiet.
                    </p>
                </div>
                <div className="grid-item">
                    <img src="https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-image-182145777.jpg" alt="profile-icon" style={{width:200 + "px"}} />
                    <figcaption style={{fontSize:20 + "px"}}>Jane Doe (No relation)</figcaption>
                    <p>
                        scelerisque et. Maecenas non nisi pellentesque, consectetur ante ac, dignissim massa. Phasellus
                        eleifend, augue at cursus scelerisque, est diam lacinia neque, nec laoreet neque mi a neque. Praesent
                        non bibendum risus. Nunc tristique massa eget mi venenatis, a sagittis mi imperdiet.
                    </p>
                </div>
                <div className="grid-item">
                    <img src="https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-image-182145777.jpg" alt="profile-icon" style={{width:200 + "px"}} />
                    <figcaption style={{fontSize:20 + "px"}}>Simon Petrikov</figcaption>
                    <p>
                        scelerisque et. Maecenas non nisi pellentesque, consectetur ante ac, dignissim massa. Phasellus
                        eleifend, augue at cursus scelerisque, est diam lacinia neque, nec laoreet neque mi a neque. Praesent
                        non bibendum risus. Nunc tristique massa eget mi venenatis, a sagittis mi imperdiet.
                    </p>
                </div>
            </div>
        </div>
    );
}

export default About;
