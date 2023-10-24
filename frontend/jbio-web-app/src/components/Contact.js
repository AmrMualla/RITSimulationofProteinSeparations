function Contact() {
    return (
        <div>
            <h1 className="page-header">Contact</h1>
            <div className="grid-container">
                <div class="grid-item">
                    <h2 className="section-header">Email</h2>
                    <ul>
                        <li>John Doe</li>
                        <ul>
                            <li>Work: email@email.com</li>
                            <li>Work: (xxx) xxx-xxxx</li>
                        </ul>
                        <li>Jane Doe</li>
                        <ul>
                            <li>Work: email@email.com</li>
                            <li>Work: (xxx) xxx-xxxx</li>
                        </ul>
                        <li>Simon Petrikov</li>
                        <ul>
                            <li>Work: email@email.com</li>
                            <li>Work: (xxx) xxx-xxxx</li>
                        </ul>
                    </ul>
                </div>
                <div class="grid-item">
                    <h2 className="section-header">Phone</h2>
                    <ul>
                        <li>John Doe</li>
                        <ul>
                            <li>Work: (xxx) xxx-xxxx</li>
                            <li>Office: (xxx) xxx-xxxx</li>
                            <li>Personal: (xxx) xxx-xxxx</li>
                        </ul>
                        <li>Jane Doe</li>
                        <ul>
                            <li>Work: (xxx) xxx-xxxx</li>
                            <li>Office: (xxx) xxx-xxxx</li>
                            <li>Personal: (xxx) xxx-xxxx</li>
                        </ul>
                    </ul>
                </div>
                <div class="grid-item">
                    <h2 className="section-header">NCBI Blast</h2>
                    <ul>
                        <li>John Doe</li>
                        <ul>
                            <li>Username: BlastUser</li>
                            <li>
                                Favorite proteins:
                                <ul>
                                    <li>Protein 1</li>
                                    <li>Protein 2</li>
                                    <li>Protein 3</li>
                                </ul>
                            </li>
                        </ul>
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default Contact;
