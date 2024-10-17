import "./AP.css"

export const AP = (props) => {
    return (
        <div className="AP-container">
            <p>{props.data.BSSID || 'N/A'}</p>
            <p>{props.data.SSID || 'N/A'}</p>
            <p>{props.data.RATE || 'N/A'}</p>
            <p>{props.data.SIGNAL || 'N/A'}</p>
        </div>
    );
}