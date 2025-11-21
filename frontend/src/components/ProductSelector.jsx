// frontend/src/components/ProductSelector.jsx
import React from 'react'

export default function ProductSelector({ products, onSelect }) {
  return (
    <div style={{ marginBottom: 16 }}>
      <label><b>Select product:</b> </label>
      <select onChange={(e) => {
        const p = products.find(x => x.id === Number(e.target.value))
        onSelect(p)
      }}>
        <option value="">-- choose --</option>
        {products.map(p => <option key={p.id} value={p.id}>{p.name}</option>)}
      </select>
    </div>
  )
}
