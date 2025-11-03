// import React, { useEffect, useState } from "react";
// import API from "../api/axios";

// function Dashboard() {
//   const [sweets, setSweets] = useState([]);

//   useEffect(() => {
//     const fetchSweets = async () => {
//       try {
//         const token = localStorage.getItem("access");
//         const res = await API.get("/sweets/", {
//           headers: { Authorization: `Bearer ${token}` },
//         });
//         setSweets(res.data);
//       } catch (error) {
//         console.error("Error fetching sweets:", error);
//       }
//     };

//     fetchSweets();
//   }, []);

//   return (
//     <div style={styles.page}>
//       <header style={styles.header}>
//         <h1 style={styles.title}>🍭 Sweet Shop Dashboard</h1>
//         <button
//           style={styles.logoutButton}
//           onClick={() => {
//             localStorage.clear();
//             window.location.href = "/";
//           }}
//         >
//           Logout
//         </button>
//       </header>

//       <div style={styles.grid}>
//         {sweets.length === 0 ? (
//           <p style={styles.empty}>No sweets available 😢</p>
//         ) : (
//           sweets.map((sweet) => (
//             <div key={sweet.id} style={styles.card}>
//               <h2 style={styles.name}>{sweet.name}</h2>
//               <p style={styles.category}>🍬 {sweet.category}</p>
//               <p style={styles.detail}>💰 Price: ₹{sweet.price}</p>
//               <p style={styles.detail}>📦 Quantity: {sweet.quantity}</p>
//               <button style={styles.button}>Buy Now</button>
//             </div>
//           ))
//         )}
//       </div>
//     </div>
//   );
// }

// const styles = {
//   page: {
//     fontFamily: "'Poppins', sans-serif",
//     background: "linear-gradient(135deg, #fff0f3, #ffe5ec)",
//     minHeight: "100vh",
//     padding: "2rem",
//   },
//   header: {
//     display: "flex",
//     justifyContent: "space-between",
//     alignItems: "center",
//     marginBottom: "2rem",
//   },
//   title: {
//     fontSize: "2rem",
//     fontWeight: "700",
//     color: "#5b2333",
//   },
//   logoutButton: {
//     backgroundColor: "#ff4d6d",
//     color: "white",
//     border: "none",
//     padding: "0.6rem 1.2rem",
//     borderRadius: "8px",
//     fontWeight: "600",
//     cursor: "pointer",
//   },
//   grid: {
//     display: "grid",
//     gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
//     gap: "1.5rem",
//   },
//   card: {
//     background: "#fff",
//     borderRadius: "15px",
//     padding: "1.5rem",
//     boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
//     transition: "transform 0.25s ease, box-shadow 0.25s ease",
//     textAlign: "center",
//   },
//   name: {
//     fontSize: "1.4rem",
//     fontWeight: "700",
//     color: "#c1121f",
//     marginBottom: "0.5rem",
//   },
//   category: {
//     fontSize: "1rem",
//     color: "#6b6b6b",
//     marginBottom: "0.5rem",
//   },
//   detail: {
//     fontSize: "1rem",
//     color: "#333",
//     margin: "0.3rem 0",
//   },
//   button: {
//     marginTop: "1rem",
//     padding: "0.6rem 1.2rem",
//     backgroundColor: "#ff8fab",
//     color: "#fff",
//     border: "none",
//     borderRadius: "8px",
//     fontWeight: "600",
//     cursor: "pointer",
//   },
//   empty: {
//     gridColumn: "1/-1",
//     textAlign: "center",
//     color: "#666",
//     fontSize: "1.2rem",
//   },
// };

// export default Dashboard;

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
