// frontend/src/api.js
const BASE = import.meta.env.VITE_API_URL || "http://localhost:8000/api";
export const fetchProducts = async () => (await fetch(`${BASE}/products`)).json();
export const fetchReviews = async (productId) => (await fetch(`${BASE}/reviews?product_id=${productId}`)).json();
export const fetchPriceHistory = async (productId) => (await fetch(`${BASE}/pricing/history?product_id=${productId}`)).json();
export const fetchEstimate = async (productId) => (await fetch(`${BASE}/pricing/estimate?product_id=${productId}`)).json();
