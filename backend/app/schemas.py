# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ProductOut(BaseModel):
    id: int
    name: str
    msrp: Optional[float]
    currency: str

class ReviewOut(BaseModel):
    id: int
    product_id: int
    reviewer_id: str
    rating: float
    title: str
    body: str
    created_at: datetime
    suspicious: Optional[bool]
    suspicious_score: Optional[float]

class PricePointOut(BaseModel):
    timestamp: datetime
    price: float

class PriceEstimateOut(BaseModel):
    product_id: int
    estimated_original_price: float
    confidence: float
    baseline_method: str
    current_price: Optional[float]
    buy_window: Optional[bool]
