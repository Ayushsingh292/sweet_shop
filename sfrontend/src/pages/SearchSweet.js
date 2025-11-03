import React from "react";

function SweetCard({ sweet, onPurchase }) {
  return (
    <div style={styles.card}>
      <h2 style={styles.name}>{sweet.name}</h2>
      <p style={styles.detail}>🍬 {sweet.category}</p>
      <p style={styles.detail}>💰 Price: ₹{sweet.price}</p>
      <p style={styles.detail}>📦 Quantity: {sweet.quantity}</p>

      <button
        onClick={onPurchase}
        disabled={sweet.quantity === 0}
        style={{
          ...styles.button,
          backgroundColor: sweet.quantity === 0 ? "#ccc" : "#ff4d6d",
          cursor: sweet.quantity === 0 ? "not-allowed" : "pointer",
        }}
      >
        {sweet.quantity === 0 ? "Out of Stock" : "Buy Now"}
      </button>
    </div>
  );
}

const styles = {
  card: {
    background: "white",
    padding: "20px",
    borderRadius: "16px",
    textAlign: "center",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    transition: "transform 0.2s",
  },
  name: {
    fontSize: "1.5rem",
    color: "#b3003b",
    marginBottom: "10px",
  },
  detail: {
    fontSize: "1rem",
    color: "#333",
    margin: "5px 0",
  },
  button: {
    marginTop: "10px",
    padding: "10px 20px",
    fontSize: "1rem",
    color: "white",
    border: "none",
    borderRadius: "8px",
    fontWeight: "bold",
  },
};

export default SweetCard;
