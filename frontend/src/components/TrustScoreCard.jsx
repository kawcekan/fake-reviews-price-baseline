// frontend/src/components/TrustScoreCard.jsx
import React from 'react'

export default function TrustScoreCard({ estimate }) {
  const buyText = estimate.buy_window ? "Good buy window" : "Wait or compare"
  return (
    <div style={{ margin: '16px 0', padding: 12, border: '1px solid #ddd', borderRadius: 8 }}>
      <b>Estimated original price:</b> ₹{estimate.estimated_original_price} &nbsp;
      <b>Confidence:</b> {Math.round(estimate.confidence * 100)}% &nbsp;
      <b>Current:</b> ₹{estimate.current_price ?? '-'} &nbsp;
      <b>Verdict:</b> {buyText}
      <div style={{ color: '#666', marginTop: 6 }}>
        Method: {estimate.baseline_method}
      </div>
    </div>
  )
}
