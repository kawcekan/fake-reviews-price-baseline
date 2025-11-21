# backend/app/routers/products.py
from fastapi import APIRouter
from ..db import get_conn
from ..schemas import ProductOut

router = APIRouter()

@router.get("/", response_model=list[ProductOut])
def list_products():
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, msrp, currency FROM products ORDER BY id")
            rows = cur.fetchall()
    conn.close()
    return [ProductOut(id=r[0], name=r[1], msrp=r[2], currency=r[3]) for r in rows]
