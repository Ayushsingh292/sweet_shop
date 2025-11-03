// import React, { useState } from "react";
// import { useNavigate } from "react-router-dom";
// import API from "../api/axios";

// function Login() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const navigate = useNavigate(); 

//   const handleLogin = async (e) => {
//     e.preventDefault();
//     try {
//       const res = await API.post("/auth/login/", { email, password });
//       localStorage.setItem("access", res.data.access);
//       localStorage.setItem("refresh", res.data.refresh);
//       alert("Login successful!");
//       navigate("/dashboard"); 
//     } catch (error) {
//       alert("Invalid credentials!");
//     }
//   };

//   return (
//     <div style={styles.container}>
//       <div style={styles.card}>
//         <h1 style={styles.title}>🍬 Sweet Shop Login</h1>
//         <form onSubmit={handleLogin} style={styles.form}>
//           <input
//             type="email"
//             placeholder="Enter your email"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//             required
//             style={styles.input}
//           />
//           <input
//             type="password"
//             placeholder="Enter your password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             required
//             style={styles.input}
//           />
//           <button type="submit" style={styles.button}>
//             Login
//           </button>
//         </form>
//         <p style={styles.footerText}>
//           Don’t have an account?{" "}
//           <a href="/register" style={styles.link}>
//             Register here
//           </a>
//         </p>
//       </div>
//     </div>
//   );
// }

// const styles = {
//   container: {
//     display: "flex",
//     justifyContent: "center",
//     alignItems: "center",
//     height: "100vh",
//     background: "linear-gradient(135deg, #ffe5ec, #fff0f3)",
//   },
//   card: {
//     backgroundColor: "white",
//     padding: "2.5rem",
//     borderRadius: "16px",
//     boxShadow: "0 6px 15px rgba(0,0,0,0.1)",
//     textAlign: "center",
//     width: "350px",
//   },
//   title: {
//     fontSize: "1.8rem",
//     fontWeight: "700",
//     color: "#6a1b4d",
//     marginBottom: "1.5rem",
//   },
//   form: {
//     display: "flex",
//     flexDirection: "column",
//     gap: "1rem",
//   },
//   input: {
//     padding: "0.8rem",
//     fontSize: "1rem",
//     borderRadius: "8px",
//     border: "1px solid #ccc",
//     outline: "none",
//     transition: "0.2s",
//   },
//   button: {
//     backgroundColor: "#ff4d6d",
//     color: "white",
//     padding: "0.8rem",
//     fontSize: "1rem",
//     fontWeight: "600",
//     border: "none",
//     borderRadius: "8px",
//     cursor: "pointer",
//     transition: "background 0.3s",
//   },
//   footerText: {
//     marginTop: "1rem",
//     fontSize: "0.9rem",
//     color: "#555",
//   },
//   link: {
//     color: "#c1121f",
//     fontWeight: "600",
//     textDecoration: "none",
//   },
// };

// export default Login;

// import React, { useState } from "react";
// import axios from "axios";
// import { useNavigate } from "react-router-dom";
// import "./Login.css";

// const Login = () => {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const navigate = useNavigate();

//   const handleLogin = async (e) => {
//     e.preventDefault();
//     try {
//       const res = await axios.post("http://127.0.0.1:8000/api/auth/login/", {
//         email,
//         password,
//       });
//       localStorage.setItem("token", res.data.access);
//       alert("Login successful!");
//       navigate("/dashboard");
//     } catch (err) {
//       alert("Invalid credentials!");
//     }
//   };

//   return (
//     <div className="login-container">
//       <div className="login-card">
//         <h2 className="title">🍬 Sweet Shop Login</h2>
//         <form onSubmit={handleLogin}>
//           <input
//             type="email"
//             placeholder="Email address"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//             required
//           />
//           <input
//             type="password"
//             placeholder="Password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             required
//           />
//           <button type="submit">Login</button>
//         </form>
//         <p className="footer">
//           Don’t have an account?{" "}
//           <a href="/register" className="register-link">
//             Register here
//           </a>
//         </p>
//       </div>
//     </div>
//   );
// };

// export default Login;

import React, { useState } from "react";
import "./Login.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/api/auth/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();
      if (response.ok) {
        localStorage.setItem("access_token", data.access);
        localStorage.setItem("refresh_token", data.refresh);
        alert("Login successful!");
        window.location.href = "/dashboard";
      } else {
        alert(data.error || "Invalid credentials!");
      }
    } catch (err) {
      alert("Server error. Please try again later.");
    }
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <h1 className="login-title">🍬 Sweet Shop Login</h1>
        <form onSubmit={handleLogin} className="login-form">
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="input-field"
          />
          <input
            type="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="input-field"
          />
          <button type="submit" className="login-btn">
            Login
          </button>
        </form>
        <p className="footer-text">
          Don’t have an account? <span className="link">Register here</span>
        </p>
      </div>
    </div>
  );
}

export default Login;
