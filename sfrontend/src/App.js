import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import AddSweet from "./pages/AddSweet";
import SearchSweet from "./pages/SearchSweet";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/add" element={<AddSweet />} />
        <Route path="/search" element={<SearchSweet />} />
      </Routes>
    </Router>
  );
}

export default App;
