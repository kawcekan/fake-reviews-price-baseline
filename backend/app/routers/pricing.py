# backend/app/routers/pricing.py
from fastapi import APIRouter, Query
from ..db import get_conn
from ..schemas import PricePointOut, PriceEstimateOut
from ..services.price_estimator import estimate_baseline

router = APIRouter()

@router.get("/history", response_model=list[PricePointOut])
def price_history(product_id: int = Query(...)):
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT timestamp, price FROM price_points
                           WHERE product_id=%s ORDER BY timestamp ASC""", (product_id,))
            rows = cur.fetchall()
    conn.close()
    return [PricePointOut(timestamp=r[0], price=r[1]) for r in rows]

@router.get("/estimate", response_model=PriceEstimateOut)
def estimate(product_id: int = Query(...)):
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT msrp, currency FROM products WHERE id=%s", (product_id,))
            msrp_row = cur.fetchone()
            cur.execute("""SELECT price, timestamp FROM price_points
                           WHERE product_id=%s ORDER BY timestamp ASC""", (product_id,))
            hist = cur.fetchall()
            cur.execute("""SELECT price FROM price_points
                           WHERE product_id=%s ORDER BY timestamp DESC LIMIT 1""", (product_id,))
            current_row = cur.fetchone()
    conn.close()
    result = estimate_baseline(msrp_row[0], hist)
    return PriceEstimateOut(product_id=product_id,
                            estimated_original_price=result["baseline"],
                            confidence=result["confidence"],
                            baseline_method=result["method"],
                            current_price=current_row[0] if current_row else None,
                            buy_window=(current_row and current_row[0] < 0.9 * result["baseline"]))
