import React, { useState } from 'react';
import '../ElectrophoresisCell.css';

const OneDE = () => {
  const [wellsCount, setWellsCount] = useState(5);

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

      <label className="wellCountLabel">Current Wells: {wellsCount}</label>  {/* Moved above the buttons */}

      <div className="buttons-container-1de">
        <button className="button1de" onClick={handleAddWell} disabled={wellsCount === 15}>
          Add Well
        </button>
        <button className="button1de" onClick={handleDropWell} disabled={wellsCount === 1}>
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
      <div className="acrylamide-gel"></div>
    </div>
  );
}

export default OneDE;
