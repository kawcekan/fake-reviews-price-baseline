# backend/app/models.py
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    msrp: Optional[float]
    currency: str

@dataclass
class Review:
    id: int
    product_id: int
    reviewer_id: str
    rating: float
    title: str
    body: str
    created_at: datetime
    suspicious: Optional[bool]
    suspicious_score: Optional[float]

@dataclass
class PricePoint:
    id: int
    product_id: int
    price: float
    timestamp: datetime
