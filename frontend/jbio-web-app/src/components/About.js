import paul from './about_images/PaulPhoto.jpg';
import beck from "./about_images/Beck_Anderson.png";
import chase from "./about_images/Chase_Amador.png";
import amr from "./about_images/Amr_Mualla.png";
import landon from "./about_images/Landon_Heatly.png";
import mack from './about_images/Mack_Leonard.png';
import placeholder from './about_images/placeholder.png';
import './About.css';

function About() {
    return (
        <div>
            <div className="navbar">
                <a href="#project-purpose"><h2 className="section-header">Project Purpose</h2></a>
                <a href="#commercial-use"><h2 className="section-header">Commercial Use</h2></a>
                <a href="#project-owner"><h2 className="section-header">Project Owner</h2></a>
                <a href="#current-developers"><h2 className="section-header">Current Developers</h2></a>
                <a href="#historic-developers"><h2 className="section-header">Historic Developers</h2></a>
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
            <div className="grid-container">
                <div className="grid-item">
                    <div style={{
                        display: 'grid',
                        justifyContent: 'center',
                        alignItems: 'center'
                    }}>
                        <img className="profile-icon" src={paul} alt="profile-icon"/>
                        <figcaption className="profile-title">Paul Craig</figcaption>
                    </div>
                    <p style={{marginLeft: "auto"}}>
                        Dr. Paul Craig received his B.S. in Chemistry from Oral Roberts University in 1979,
                        and his Ph.D. in Biological Chemistry from The University of Michigan in 1985.
                        Following a post-doc at Henry Ford Hospital (biophysical chemistry of blood clotting;
                        1985-1988), he spent five years as an analytical biochemistry at BioQuant, Inc., in
                        Ann Arbor, Michigan before joining RIT in 1993.
                    </p>
                </div>
            </div>
            <h2 className="section-header" id="current-developers">Current Developers</h2>
            <div className="grid-container">
                <div className="grid-item">
                    <img className="profile-icon" src={chase} alt="profile-icon"/>
                    <figcaption className="profile-title">Chase Amador</figcaption>
                    <p>
                        Bio here...
                    </p>
                </div>
                <div className="grid-item">
                    <img className="profile-icon" src={beck} alt="profile-icon"/>
                    <figcaption className="profile-title">Beck Anderson</figcaption>
                    <p>
                        Bio here...
                    </p>
                </div>
                <div className="grid-item">
                    <img className="profile-icon" src={landon} alt="profile-icon"/>
                    <figcaption className="profile-title">Landon Heatly</figcaption>
                    <p>
                        Bio here...
                    </p>
                </div>
                <div className="grid-item">
                    <img className="profile-icon" src={mack} alt="profile-icon"/>
                    <figcaption className="profile-title">Mack Leonard</figcaption>
                    <p>
                        Bio here...
                    </p>
                </div>
                <div className="grid-item">
                    <img className="profile-icon" src={amr} alt="profile-icon"/>
                    <figcaption className="profile-title">Amr Mualla</figcaption>
                    <p>
                        Bio here...
                    </p>
                </div>
            </div>
            <h2 className="section-header" id="historic-developers">Historic Developers</h2>
            <div className="historic-grid">
                <div className="historic-grid-item">
                    <img className="historic-icon" src={placeholder} alt="profile-icon"/>
                    <figcaption className="historic-title">Place Holder</figcaption>
                    <p>
                        Bio here...
                    </p>
                </div>
            </div>
        </div>
    );
}

export default About;
