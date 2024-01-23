import React, { useState } from 'react';
import '../ElectrophoresisCell.css';

const OneDE = () => {
  const [wellsCount, setWellsCount] = useState(5);
  const [acrylamidePercentage, setAcrylamidePercentage] = useState('7.5%');
  const [voltageValue, setvoltageValue] = useState('50V');
  const [folderUpload, setFolderUpload] = useState(false);
  const [selectedProtein, setSelectedProtein] = useState(null);
  const [animationInProgress, setAnimationInProgress] = useState(false);

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
    { name: "B-Galactosidase", molecularWeight: 116250, velocity: 100, color: '#08c8ae' },
    { name: "Phosphorylase B", molecularWeight: 97400, velocity: 25, color: '#cacf50' },
    { name: "Serum Albumin", molecularWeight: 66200, velocity: 7.6, color: '#41add5' },
    { name: "Ovalbumin", molecularWeight: 45000, velocity: 4, color: '#a6106a' },
    { name: "Carbonic Anhydrase", molecularWeight: 31000, velocity: 19, color: '#87cba7' },
    { name: "Trypsin Inhibitor", molecularWeight: 21500, velocity: 14, color: '#180ea4' },
    { name: "Lysozyme", molecularWeight: 14400, velocity: 10, color: '#2e8c7b' },
    { name: "Aprotinin", molecularWeight: 6500, velocity: 2, color: '#be2908' }
  ];
  
  
  const startAnimation = () => {
    if (animationInProgress) {
      proteinStandards.forEach(protein => {
        document.querySelectorAll(`.well .protein-${protein.name}`)
          .forEach(element => {
            element.style.animationPlayState = 'running';
          });
      });
    } else {
      setAnimationInProgress(true);
      proteinStandards.forEach(protein => {
        const duration = `${protein.velocity}s`;
        document.querySelectorAll(`.well .protein-${protein.name}`)
          .forEach(element => {
            element.style.animation = `moveProtein ${duration} linear forwards`;
          });
      });
    }
  };
  
  
  
  const handleStop = () => {
    proteinStandards.forEach(protein => {
      document.querySelectorAll(`.well .protein-${protein.name}`)
        .forEach(element => {
          element.style.animationPlayState = 'paused';
        });
    });
    setAnimationInProgress(false); 
  };
  
  
  const handleRefillWells = () => {
    proteinStandards.forEach(protein => {
      document.querySelectorAll(`.well .protein-${protein.name}`)
        .forEach(element => {
          element.style.animation = 'none'; 
        });
    });
    setAnimationInProgress(false);
  };
  
  
  const handleClearWells = () => {
    // Logic to clear wells
  };
  

  return (
    
    <div className="electrophoresis-wrapper">
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
                {idx === 0 && proteinStandards.map((protein, index) => (
                  <div key={index} 
                      className={`proteinBand protein-${protein.name}`}
                      onClick={() => handleProteinClick(protein)}
                      style={{ cursor: 'pointer', backgroundColor: protein.color }}>
                    {/* Protein band content */}
                  </div>
                ))}
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
          <option value="15%">15%</option>
        </select>
      </div>
    </div>
  );
}

export default OneDE;
