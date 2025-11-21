# backend/app/services/review_rules.py
import math
from datetime import datetime, timedelta

EXTREME_WORDS = {"amazing", "perfect", "best", "worst", "awful", "scam", "must buy", "life changing"}

def rule_based_score(text: str, rating: float, reviewer_id: str, created_at: datetime) -> float:
    score = 0.0
    # Sentiment extremes
    extremes = sum(w in text for w in EXTREME_WORDS)
    score += min(extremes * 0.1, 0.3)
    # Rating-text mismatch
    if rating >= 4.5 and ("bad" in text or "issue" in text or "return" in text):
        score += 0.2
    if rating <= 2.0 and ("amazing" in text or "great" in text):
        score += 0.2
    # Reviewer metadata heuristic (e.g., anonymous or repeated)
    if reviewer_id.startswith("guest_") or reviewer_id.endswith("_temp"):
        score += 0.15
    # Burstiness: reviews within short window get more suspicion (requires app-level context; simple decay here)
    recency_factor = max(0.0, 1.0 - min(30, (datetime.utcnow() - created_at).days) / 30.0)
    score += recency_factor * 0.15
    # Length anomalies
    if len(text.split()) < 4 or len(text.split()) > 300:
        score += 0.1
    return min(score, 1.0)
