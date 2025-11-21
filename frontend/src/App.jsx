// frontend/src/App.jsx
import React, { useEffect, useState } from 'react'
import { fetchProducts, fetchReviews, fetchPriceHistory, fetchEstimate } from './api'
import ProductSelector from './components/ProductSelector'
import TrustScoreCard from './components/TrustScoreCard'
import ReviewTable from './components/ReviewTable'
import PriceChart from './components/PriceChart'

export default function App() {
  const [products, setProducts] = useState([])
  const [selected, setSelected] = useState(null)
  const [reviews, setReviews] = useState([])
  const [history, setHistory] = useState([])
  const [estimate, setEstimate] = useState(null)

  useEffect(() => { fetchProducts().then(setProducts) }, [])
  useEffect(() => {
    if (!selected) return
    fetchReviews(selected.id).then(setReviews)
    fetchPriceHistory(selected.id).then(setHistory)
    fetchEstimate(selected.id).then(setEstimate)
  }, [selected])

  return (
    <div style={{ padding: 24, fontFamily: 'system-ui' }}>
      <h2>Trust & Price Dashboard</h2>
      <p>Building trust in online shopping</p>
      <ProductSelector products={products} onSelect={setSelected} />
      {selected && estimate && (
        <>
          <TrustScoreCard estimate={estimate} />
          <PriceChart history={history} estimate={estimate} currency={selected.currency} />
          <ReviewTable reviews={reviews} />
        </>
      )}
    </div>
  )
}
