import React, {useState,useEffect} from 'react'
import './App.css';
import {AP} from "./components/AP.jsx"
import io from 'socket.io-client';
function App() {
  const [data,setData] = useState([{}])
   const [isConnected, setIsConnected] = useState(false);
 useEffect(() => {
    // Connect to the WebSocket server
    const socket = io('http://127.0.0.1:5000'); // Adjust to your backend URL if different

    // Listen for connection events
    socket.on('connect', () => {
      console.log('Successfully connected to the WebSocket server');
      setIsConnected(true);
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from the WebSocket server');
      setIsConnected(false);
    });

    // Listen for 'update' events from the backend
    socket.on('update', (message) => {
      setData(message.data);
      console.log('Received data:', message.data);
    });

    // Listen for connection error events
    socket.on('connect_error', (error) => {
      console.error('Connection Error:', error);
    });

    // Cleanup: Disconnect socket when component unmounts
    return () => socket.disconnect();
  }, []);

  return (
      <div className="App">
          {
            data.map((element)=> <AP data={element}></AP>)
          }
      </div>

  );
}

export default App;
