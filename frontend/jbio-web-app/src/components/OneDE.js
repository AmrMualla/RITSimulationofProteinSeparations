import React, { useState } from 'react';
import '../ElectrophoresisCell.css';

const OneDE = () => {
  const [wellsCount, setWellsCount] = useState(10);
  const [acrylamidePercentage, setAcrylamidePercentage] = useState('7.5%');
  const [voltageValue, setvoltageValue] = useState('50V');
  const [folderUpload, setFolderUpload] = useState(false);
  const [selectedProtein, setSelectedProtein] = useState(null);
  const [animationInProgress, setAnimationInProgress] = useState(false);
  const [isAtStartingPoint, setIsAtStartingPoint] = useState(true);

  const handleAddWell = () => {
    if (wellsCount < 15) {
      setWellsCount(wellsCount + 1);
    }
  };

  const handleDropWell = () => {
    if (wellsCount > 1) {
      setWellsCount(wellsCount - 1);
    }
  };

  const handleProteinClick = (protein) => {
    setSelectedProtein(protein);
  };

  const proteinStandards = [
    { name: "B-Galactosidase", molecularWeight: 116250, velocity: 300, color: '#08c8ae' },
    { name: "Phosphorylase B", molecularWeight: 97400, velocity: 25, color: '#cacf50' },
    { name: "Serum Albumin", molecularWeight: 66200, velocity: 7.6, color: '#41add5' },
    { name: "Ovalbumin", molecularWeight: 45000, velocity: 4, color: '#a6106a' },
    { name: "Carbonic Anhydrase", molecularWeight: 31000, velocity: 19, color: '#87cba7' },
    { name: "Trypsin Inhibitor", molecularWeight: 21500, velocity: 5, color: '#180ea4' },
    { name: "Lysozyme", molecularWeight: 14400, velocity: 10, color: '#2e8c7b' },
    { name: "Aprotinin", molecularWeight: 6500, velocity: 2.6, color: '#be2908' },
    { name: "BlueDye", molecularWeight: 500, velocity: 2, color: '#0000FF' }
  ];
  
  const initialMoveDuration = 1;
  const startAnimation = () => {
    if (!animationInProgress && isAtStartingPoint) {
      setAnimationInProgress(true);
      setIsAtStartingPoint(false);
  
      let blueDyeDuration = 0;
  
      proteinStandards.forEach(protein => {
        const elementSelector = `.well .protein-${protein.name.replace(/\s+/g, '-')}`;
        const initialDurationSeconds = 1; 
        const moveDuration = protein.velocity;
  
        if (protein.name === 'BlueDye') {
          // For BlueDye, calculate the total duration including the initial movement and the main movement
          blueDyeDuration = (initialDurationSeconds + moveDuration) * 1000; 
        }
        document.querySelectorAll(elementSelector).forEach(element => {
          element.style.animation = `initialMove ${initialDurationSeconds}s linear forwards`;
        });
        setTimeout(() => {
          document.querySelectorAll(elementSelector).forEach(element => {
            element.style.animation = `moveProtein ${moveDuration}s linear forwards`;
          });
        }, initialDurationSeconds * 1000); 
      });
      // Use blueDyeDuration to stop all animations when BlueDye is @ bottom
      setTimeout(() => {
        stopAllProteins();
      }, blueDyeDuration);
    }
  };

  
  const stopAllProteins = () => {
    proteinStandards.forEach(protein => {
      document.querySelectorAll(`.well .protein-${protein.name.replace(/\s+/g, '-')}`)
        .forEach(element => {
          element.style.animationPlayState = 'paused';
        });
    });
    setAnimationInProgress(false);
  };
  
  
  const handleStop = () => {
    proteinStandards.forEach(protein => {
      document.querySelectorAll(`.well .protein-${protein.name.replace(/\s+/g, '-')}`)
        .forEach(element => {
          element.style.animationPlayState = 'paused';
        });
    });
    setAnimationInProgress(false); 
  };
  
  
  const handleRefillWells = () => {
    proteinStandards.forEach(protein => {
      document.querySelectorAll(`.well .protein-${protein.name.replace(/\s+/g, '-')}`)
        .forEach(element => {
          element.style.animation = 'none';
        });
    });
  
    setAnimationInProgress(false);
    setIsAtStartingPoint(true); 
  };
  
  
  const [selectedProteins, setSelectedProteins] = useState(proteinStandards.map(protein => protein.name));

  
  const handleClearWells = () => {
    // Logic to clear wells
  };

  const handleProteinSelection = (event, proteinName) => {
    if (event.target.checked) {
      setSelectedProteins([...selectedProteins, proteinName]);
    } else {
      setSelectedProteins(selectedProteins.filter(name => name !== proteinName));
    }
  };
  
  

  return (
    
    <div className="electrophoresis-wrapper">
        <div className="protein-selection">
            {proteinStandards.map((protein, index) => (
              <div key={index} className="protein-checkbox">
                <input
                  type="checkbox"
                  id={`protein-${index}`}
                  checked={selectedProteins.includes(protein.name)}
                  onChange={(e) => handleProteinSelection(e, protein.name)}
                  disabled={!isAtStartingPoint} // Disable checkbox unless at the starting point
                />
                <label htmlFor={`protein-${index}`}>{protein.name}</label>
              </div>
            ))}
        </div>
        {selectedProtein && (
          <div className="protein-info">
            <button onClick={() => setSelectedProtein(null)} className="close-button">X</button>
            <h3>Protein Information</h3>
            <p>Name: {selectedProtein.name}</p>
            <p>Molecular Weight: {selectedProtein.molecularWeight}</p>
          </div>
        )}
        <div className="control-buttons-container">
          <button onClick={startAnimation} className="control-button">Start</button>
          <button onClick={handleStop} className="control-button">Stop</button>
          <button onClick={handleRefillWells} className="control-button">Refill Wells</button>
          <button onClick={handleClearWells} className="control-button">Clear Wells</button>
        </div>
      <img src="/blackwirelength.png" alt="Black Wire Extension in Center" className="blackwireextendedmiddle-image" />
      <img src="/redwirelength.png" alt="Red Wire Extension in Center" className="redwireextendedmiddle-image" />
      <img src="/redwirelength.png" alt="Red Wire Extension" className="redwireextendedhorizontal-image" />
      <img src="/blackwirelength.png" alt="Black Wire Extension" className="blackwireextendedhorizontal-image" />
      <img src="/blackwirelength.png" alt="Black Wire Extension" className="blackwireextended-image" />
      <div className='uploadContainer'>
        <div className='uploadTypeContainer'>
          <button onClick={() => setFolderUpload(false)} className="typeFile" style={folderUpload ? {} : {border:"black 1px solid", backgroundColor:"#2253e7"}}>File</button>
          <button onClick={() => setFolderUpload(true)} className="typeFolder" style={folderUpload ? {border:"black 1px solid", backgroundColor:"#2253e7"} : {}}>Folder</button>
        </div>
        <form className='upload'>
          { !folderUpload && (
            <div style={{width:15 + 'em', paddingTop:10 + 'px'}}>
              <label htmlFor="uploaded" className="submitUpload" style={{marginBottom:-50 + 'px'}}>Select File</label>
              <input type="file" id="uploaded" style={{visibility:'hidden'}} />
            </div>
          )}
          { folderUpload && (
            <div style={{width:15 + 'em', paddingTop:10 + 'px'}}>
              <label htmlFor="uploaded" className="submitUpload">Select Folder</label>
              <input type="file" id="uploaded" style={{visibility:'hidden'}} webkitdirectory="" />
            </div>
          )}
          <input className="submitUpload" type="submit" />
        </form>
      </div>
      <div className="voltage-dropdown-section">
        <select value={voltageValue} onChange={e => setvoltageValue(e.target.value)}>
          <option value="50V">50V</option>
          <option value="100V">100V</option>
          <option value="150V">150V</option>
          <option value="200V">200V</option>
        </select>
      </div>
      <label className="voltage-value-label">Voltage: </label>
      <img src="/redwirelength.png" alt="Red Wire Extension" className="redwireextended-image" />
      <img src="/redwire.png" alt="Red Wire" className="redwire-image" />
      <img src="/blackwire.png" alt="Black Wire" className="blackwire-image" />
      <label className="wellCountLabel">Current Wells: {wellsCount}</label>
      <label className="acrylamide-percentage-label">Acrylamide %: </label>
      <div className="options-box"></div>
      <div className="buttons-container-1de">
        <button className="button1deadd" onClick={handleAddWell} disabled={wellsCount === 15}>
          Add Well
        </button>
        <button className="button1dedrop" onClick={handleDropWell} disabled={wellsCount === 1}>
          Drop Well
        </button>
      </div>
      
      <div className="electrophoresis-cell">
        <div className="wells-container">
          {Array.from({ length: wellsCount }).map((_, idx) => (
            <React.Fragment key={idx}>
              { idx !== 0 && <div className="divider"></div> }
              <div className="well">
                  <form action="/" className="wellForm">
                    <input type="file" className="wellInput" style={{opacity:0, position: "absolute", top:0, left:0, bottom:0, right:0, width:100+"%", height:100+"%"}} />
                  </form>
              
                  {idx === 0 && selectedProteins.map((proteinName, index) => {
                    const protein = proteinStandards.find(p => p.name === proteinName);
                    return (
                      <div key={index} 
                        className={`proteinBand protein-${protein.name.replace(/\s+/g, '-')}`}
                        onClick={() => handleProteinClick(protein)}
                        style={{ cursor: 'pointer', backgroundColor: protein.color }}>
                        {/* Protein band content */}
                      </div>
                    );
                  })}
              </div>
            </React.Fragment>
          ))}
        </div>
      </div>
      <div className="acrylamide-gel-top"></div>
      <div className="acrylamide-gel-bottom"></div>

      <label className="acrylamide-label">Acrylamide: {acrylamidePercentage}</label>  {/* Acrylamide label */}
      <label className="voltage-label">{voltageValue}</label>
      <div className="acrylamide-dropdown-section">
        <select value={acrylamidePercentage} onChange={e => setAcrylamidePercentage(e.target.value)}>
          <option value="7.5%">7.5%</option>
          <option value="10%">10%</option>
          <option value="12%">12%</option>
          <option value="15%">15%</option>
        </select>
      </div>
    </div>
  );
}

export default OneDE;
