import React, { useState, useEffect } from 'react';
import './App.css';
import { AP } from "./components/AP.jsx";

function App() {
  const [data, setData] = useState([]);
  const [sortedData, setSortedData] = useState([]);
  const [sortCriteria, setSortCriteria] = useState(null); // Store current sorting criteria

  useEffect(() => {
    const fetchData = () => {
      fetch("http://127.0.0.1:5000/PickYourWifi")
        .then(res => res.json())
        .then(receivedData => {
          setData(receivedData);
          // Maintain the current sorted state based on previous criteria
          if (sortCriteria === 'rate') {
            sortByRate(receivedData);
          } else if (sortCriteria === 'signal') {
            sortBySignal(receivedData);
          } else {
            setSortedData(receivedData); // Default to unsorted data
          }
          console.log("Received data:", receivedData);
        })
        .catch(error => console.error("Error fetching data:", error));
    };

    fetchData();

    const intervalId = setInterval(fetchData, 1000);

    return () => clearInterval(intervalId);
  }, [sortCriteria]); // Add sortCriteria to dependencies

  const sortByRate = (dataToSort) => {
    const sorted = [...dataToSort].sort((a, b) => {
      const rateA = parseFloat(a.RATE) || 0;
      const rateB = parseFloat(b.RATE) || 0;
      return rateB - rateA; // Sort descending
    });
    setSortedData(sorted);
    setSortCriteria('rate'); // Update sorting criteria
  };

  const sortBySignal = (dataToSort) => {
    const sorted = [...dataToSort].sort((a, b) => {
      const signalA = parseFloat(a.SIGNAL) || 0;
      const signalB = parseFloat(b.SIGNAL) || 0;
      return signalB - signalA; // Sort descending
    });
    setSortedData(sorted);
    setSortCriteria('signal'); // Update sorting criteria
  };

  return (
    <div className="App">
      <div className="title">APtracker</div>
      <div className="sort-buttons">
        <button
          onClick={() => sortByRate(data)}
          className={sortCriteria === 'rate' ? 'active' : ''}
        >
          Sort by Rate
        </button>
        <button
          onClick={() => sortBySignal(data)}
          className={sortCriteria === 'signal' ? 'active' : ''}
        >
          Sort by Signal
        </button>
      </div>
      {sortedData.map((element, index) => (
        <AP key={index} data={element} />
      ))}
    </div>
  );
}

export default App;
