# backend/app/routers/reviews.py
from fastapi import APIRouter, Query
from ..db import get_conn
from ..schemas import ReviewOut
from ..services.review_detector import score_review_row

router = APIRouter()

@router.get("/", response_model=list[ReviewOut])
def list_reviews(product_id: int = Query(...)):
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT id, product_id, reviewer_id, rating, title, body, created_at
                           FROM reviews WHERE product_id=%s ORDER BY created_at DESC""", (product_id,))
            rows = cur.fetchall()
    conn.close()
    out = []
    for r in rows:
        score = score_review_row(r[2], r[3], r[4], r[5], r[6])
        out.append(ReviewOut(id=r[0], product_id=r[1], reviewer_id=r[2], rating=r[3],
                             title=r[4], body=r[5], created_at=r[6],
                             suspicious=score["suspicious"], suspicious_score=score["score"]))
    return out
