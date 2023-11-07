import React, { useState } from 'react';
import '../ElectrophoresisCell.css';

const OneDE = () => {
  const [wellsCount, setWellsCount] = useState(5);
  const [acrylamidePercentage, setAcrylamidePercentage] = useState('7.5%');

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

  return (
    <div className="electrophoresis-wrapper">
      
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
              <div className="well"></div>
            </React.Fragment>
          ))}
        </div>
      </div>
      <div className="acrylamide-gel-top"></div>
      <div className="acrylamide-gel-bottom"></div>

      <label className="acrylamide-label">Acrylamide: {acrylamidePercentage}</label>  {/* Acrylamide label */}
      
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
