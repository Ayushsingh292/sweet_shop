

import React, { useEffect, useState } from "react";
import "./Dashboard.css";

function Dashboard() {
  const [sweets, setSweets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchSweets = async () => {
      try {
        const token = localStorage.getItem("access_token");
        if (!token) {
          setError("No token found. Please login again.");
          setLoading(false);
          return;
        }

        const response = await fetch("http://127.0.0.1:8000/api/sweets/", {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });

        const data = await response.json();
        if (response.ok) setSweets(data);
        else setError(data.error || "Failed to fetch sweets.");
      } catch {
        setError("Server connection error.");
      } finally {
        setLoading(false);
      }
    };

    fetchSweets();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    window.location.href = "/";
  };

  if (loading)
    return <div className="loading">🍬 Loading your sweets...</div>;

  if (error)
    return (
      <div className="error-page">
        <p>{error}</p>
        <button onClick={handleLogout}>Go to Login</button>
      </div>
    );

  return (
    <div className="dashboard">
      <div className="header">
        <h1>🍭 Sweet Shop Dashboard</h1>
        <button onClick={handleLogout} className="logout-btn">
          Logout
        </button>
      </div>

      {sweets.length === 0 ? (
        <p className="no-sweets">No sweets available 😢</p>
      ) : (
        <div className="sweet-grid">
          {sweets.map((sweet, index) => (
            <div key={index} className="sweet-card">
              <h2>{sweet.name}</h2>
              <p>🍡 Category: {sweet.category}</p>
              <p>💰 Price: ₹{sweet.price}</p>
              <p>🧁 Quantity: {sweet.quantity}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Dashboard;
