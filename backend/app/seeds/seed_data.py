# backend/app/seeds/seed_data.py
from datetime import datetime, timedelta
from ..db import get_conn

def seed():
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM price_points; DELETE FROM reviews; DELETE FROM products;")
            cur.execute("INSERT INTO products (name, msrp, currency) VALUES (%s, %s, %s) RETURNING id",
                        ("Wireless Headphones", 3499, "INR"))
            pid = cur.fetchone()[0]

            # Price history (simulate discounts and regimes)
            base_date = datetime.utcnow() - timedelta(days=60)
            prices = [3499, 3499, 3399, 3299, 3199, 2999, 2899, 2999, 2799, 2899,
                      2699, 2799, 2899, 2999, 2899, 2799, 2899, 2999, 2899, 2899]
            for i, p in enumerate(prices):
                cur.execute("INSERT INTO price_points (product_id, price, timestamp) VALUES (%s, %s, %s)",
                            (pid, p, base_date + timedelta(days=i*3)))

            # Reviews
            reviews = [
                ("guest_123", 5, "Amazing product!", "Perfect sound, must buy", base_date + timedelta(days=5)),
                ("user_anna", 4, "Great value", "Good battery and comfort", base_date + timedelta(days=10)),
                ("user_bob", 1.5, "Worst", "Awful, but amazing? returned", base_date + timedelta(days=12)),
                ("guest_temp", 5, "Best ever", "Life changing purchase", base_date + timedelta(days=15)),
                ("user_dev", 3.5, "Solid", "Decent for the price", base_date + timedelta(days=21)),
            ]
            for r in reviews:
                cur.execute("""INSERT INTO reviews (product_id, reviewer_id, rating, title, body, created_at)
                               VALUES (%s, %s, %s, %s, %s, %s)""", (pid, *r))
    conn.close()

if __name__ == "__main__":
    seed()
