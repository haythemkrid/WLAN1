import React, { useState, useEffect } from 'react';
import './App.css';
import { AP } from "./components/AP.jsx";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    const fetchData = () => {
      fetch("http://127.0.0.1:5000/PickYourWifi") // Adjust to your backend URL if different
        .then(res => res.json())
        .then(receivedData => {
          setData(receivedData);
          console.log("Received data:", receivedData);
        })
        .catch(error => console.error("Error fetching data:", error));
    };

    // Fetch data initially
    fetchData();

    // Set up interval to fetch data every 1 second (1000 ms)
    const intervalId = setInterval(fetchData, 1000);

    // Clean up: clear interval on component unmount
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="App">
      <div className="title">
        APtracker
      </div>


      {data.map((element, index) => (
        <AP key={index} data={element} />
      ))}
    </div>
  );
}

export default App;
