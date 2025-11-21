# backend/app/services/price_estimator.py
import numpy as np
from ..config import MSRP_WEIGHT, HIST_WEIGHT

def robust_median(prices):
    return float(np.median(prices)) if prices else None

def detect_regimes(prices):
    # Simple regime segmentation: split on large jumps >25%
    if not prices or len(prices) < 6:
        return [prices]
    segments = []
    seg = [prices[0]]
    for p in prices[1:]:
        if abs(p - seg[-1]) / max(1e-9, seg[-1]) > 0.25 and len(seg) >= 3:
            segments.append(seg)
            seg = [p]
        else:
            seg.append(p)
    if seg:
        segments.append(seg)
    return segments

def estimate_baseline(msrp, hist_rows):
    prices = [float(p) for p, ts in hist_rows]
    if not prices:
        baseline = msrp if msrp else 0.0
        return {"baseline": baseline, "confidence": 0.5 if msrp else 0.2, "method": "msrp_only"}
    regimes = detect_regimes(prices)
    recent_regime = regimes[-1] if regimes else prices
    hist_med = robust_median(recent_regime)
    if msrp:
        baseline = MSRP_WEIGHT * msrp + HIST_WEIGHT * hist_med
        confidence = 0.7 + 0.2 * min(1.0, len(recent_regime)/20.0)
        method = "msrp_hist_blend"
    else:
        baseline = hist_med
        confidence = 0.6 + 0.2 * min(1.0, len(recent_regime)/20.0)
        method = "hist_median"
    return {"baseline": float(round(baseline, 2)), "confidence": float(round(confidence, 2)), "method": method}
