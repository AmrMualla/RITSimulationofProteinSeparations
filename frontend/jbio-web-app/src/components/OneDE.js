import React, { useState } from 'react';
import '../ElectrophoresisCell.css';

const OneDE = () => {
  const [wellsCount, setWellsCount] = useState(10); // Initial count set to 10

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
            <div key={idx} className="well"></div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default OneDE;
