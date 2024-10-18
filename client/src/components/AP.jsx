import "./AP.css";
import WifiIcon from './WifiIcon';

export const AP = (props) => {
    const { BSSID, SSID, RATE, SIGNAL, MODE, SECURITY, ["IN-USE"]: inUse } = props.data;

    // Determine if the access point is in use
    const isInUse = inUse === '*';

    return (
        <div className={`AP-container ${isInUse ? 'in-use' : ''}`}>
            <p>{SSID || 'N/A'}</p>
            <p>{SECURITY || 'N/A'}</p>
            <p>{RATE || 'N/A'}</p>
            <WifiIcon signalStrength={SIGNAL ? Math.floor(SIGNAL / 20) : 0} />
        </div>
    );
};

