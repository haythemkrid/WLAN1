import React from 'react';
import './WifiIcon.css'; // Ensure you have the correct path for your CSS file

const WifiIcon = ({ signalStrength }) => {
    return (
        <div className="wifi-icon">
            <div className={`wifi-bar ${signalStrength >= 1 ? 'active' : ''}`}></div>
            <div className={`wifi-bar ${signalStrength >= 2 ? 'active' : ''}`}></div>
            <div className={`wifi-bar ${signalStrength >= 3 ? 'active' : ''}`}></div>
            <div className={`wifi-bar ${signalStrength >= 4 ? 'active' : ''}`}></div>
            <div className={`wifi-bar ${signalStrength >= 5 ? 'active' : ''}`}></div>
        </div>
    );
};

export default WifiIcon;
