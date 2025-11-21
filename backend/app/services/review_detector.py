# backend/app/services/review_detector.py
from . import review_rules
from ..utils.preprocessing import clean_text

def score_review_row(reviewer_id: str, rating: float, title: str, body: str, created_at):
    text = clean_text((title or "") + " " + (body or ""))
    rule_score = review_rules.rule_based_score(text, rating, reviewer_id, created_at)
    suspicious = rule_score >= 0.6
    return {"score": float(rule_score), "suspicious": suspicious}
