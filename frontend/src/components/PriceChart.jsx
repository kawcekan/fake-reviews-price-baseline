// frontend/src/components/PriceChart.jsx
import React, { useEffect, useRef } from 'react'
import Plotly from 'plotly.js'

export default function PriceChart({ history, estimate, currency }) {
  const ref = useRef()
  useEffect(() => {
    const x = history.map(h => new Date(h.timestamp))
    const y = history.map(h => h.price)
    const baseline = y.map(() => estimate.estimated_original_price)
    Plotly.newPlot(ref.current, [
      { x, y, type: 'scatter', mode: 'lines+markers', name: 'Price history' },
      { x, y: baseline, type: 'scatter', mode: 'lines', name: 'Baseline', line: { dash: 'dot', color: 'red' } }
    ], { title: `Price history (${currency})`, margin: { t: 40 } }, { responsive: true })
  }, [history, estimate, currency])
  return <div ref={ref} />
}
