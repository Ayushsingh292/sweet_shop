import React from "react";

function SweetCard({ sweet }) {
  return (
    <div className="sweet-card">
      <h3>{sweet.name}</h3>
      <p>Category: {sweet.category}</p>
      <p>Price: ₹{sweet.price}</p>
      <p>Quantity: {sweet.quantity}</p>
    </div>
  );
}

export default SweetCard;
