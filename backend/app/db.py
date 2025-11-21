# backend/app/db.py
import psycopg2
from .config import DB_URL

def get_conn():
    return psycopg2.connect(DB_URL)

def init_db():
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute(open("/db/init.sql", "r").read())
    conn.close()
