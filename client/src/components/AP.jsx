
import "./AP.css";
import WifiIcon from './WifiIcon'; // Import the WifiIcon component

export const AP = (props) => {
    const { BSSID, SSID, RATE, SIGNAL } = props.data;

    return (
        <div className="AP-container">
            <p>{BSSID || 'N/A'}</p>
            <p>{SSID || 'N/A'}</p>
            <p>{RATE || 'N/A'}</p>
            <p>{SIGNAL || 'N/A'}</p>
            <WifiIcon signalStrength={SIGNAL ? Math.floor(SIGNAL / 20) : 0} />
        </div>
    );
};
