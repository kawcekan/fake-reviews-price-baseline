// frontend/src/components/ReviewTable.jsx
import React from 'react'

export default function ReviewTable({ reviews }) {
  return (
    <div style={{ marginTop: 24 }}>
      <h3>Reviews</h3>
      <table border="1" cellPadding="6" style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th>Reviewer</th><th>Rating</th><th>Title</th><th>Suspicious</th><th>Score</th><th>Date</th>
          </tr>
        </thead>
        <tbody>
          {reviews.map(r => (
            <tr key={r.id}>
              <td>{r.reviewer_id}</td>
              <td>{r.rating}</td>
              <td>{r.title}</td>
              <td>{r.suspicious ? 'Yes' : 'No'}</td>
              <td>{(r.suspicious_score ?? 0).toFixed(2)}</td>
              <td>{new Date(r.created_at).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
