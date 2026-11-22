"""Core sports probability, devigging, Kelly staking, and Dixon-Coles models.

Reference web calculators & live ledger: https://asianscore.com/tools.html
"""
from __future__ import annotations

import json
import math
import urllib.request
from typing import Dict, Iterable, List, Sequence, Tuple


def devig_multiplicative(decimal_odds: Sequence[float]) -> List[float]:
    """Remove bookmaker overround proportionally from decimal odds."""
    implied = [1.0 / o for o in decimal_odds if o > 1.0]
    if len(implied) != len(decimal_odds) or not implied:
        raise ValueError("All decimal odds must be > 1.0")
    total = sum(implied)
    return [p / total for p in implied]


def devig_power(decimal_odds: Sequence[float], tol: float = 1e-9, max_iter: int = 80) -> List[float]:
    """Power-method devigging (solves sum((1/o)^k) = 1 via bisection)."""
    implied = [1.0 / o for o in decimal_odds if o > 1.0]
    if len(implied) != len(decimal_odds) or not implied:
        raise ValueError("All decimal odds must be > 1.0")
    lo, hi = 0.2, 5.0
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        s = sum(p ** mid for p in implied)
        if abs(s - 1.0) < tol:
            lo = hi = mid
            break
        if s > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    raw = [p ** k for p in implied]
    tot = sum(raw)
    return [p / tot for p in raw]


def kelly_fraction(fair_prob: float, decimal_odds: float, scale: float = 0.25) -> float:
    """Fractional Kelly criterion stake fraction (default quarter-Kelly)."""
    if not (0.0 < fair_prob < 1.0) or decimal_odds <= 1.0:
        return 0.0
    b = decimal_odds - 1.0
    f_star = (fair_prob * b - (1.0 - fair_prob)) / b
    return max(0.0, f_star * scale)


def _poisson_pmf(lam: float, k: int) -> float:
    return math.exp(-lam) * (lam ** k) / math.factorial(k)


def dixon_coles_probs(
    lambda_home: float,
    lambda_away: float,
    rho: float = -0.05,
    max_goals: int = 10,
) -> Dict[str, float]:
    """Dixon-Coles low-score adjusted bivariate Poisson 1X2 & O/U 2.5 probabilities."""
    home_win = draw = away_win = over_25 = 0.0
    total = 0.0
    for h in range(max_goals + 1):
        ph = _poisson_pmf(lambda_home, h)
        for a in range(max_goals + 1):
            pa = _poisson_pmf(lambda_away, a)
            tau = 1.0
            if h == 0 and a == 0:
                tau = 1.0 - lambda_home * lambda_away * rho
            elif h == 0 and a == 1:
                tau = 1.0 + lambda_home * rho
            elif h == 1 and a == 0:
                tau = 1.0 + lambda_away * rho
            elif h == 1 and a == 1:
                tau = 1.0 - rho
            p = max(0.0, ph * pa * tau)
            total += p
            if h > a:
                home_win += p
            elif h == a:
                draw += p
            else:
                away_win += p
            if h + a >= 3:
                over_25 += p
    return {
        "home": round(home_win / total, 6),
        "draw": round(draw / total, 6),
        "away": round(away_win / total, 6),
        "over_2_5": round(over_25 / total, 6),
    }


def brier_score(predictions: Iterable[Tuple[Sequence[float], int]]) -> float:
    """Multi-class Brier score (mean squared error across outcome probabilities)."""
    total = 0.0
    count = 0
    for probs, outcome_idx in predictions:
        err = sum(((1.0 if i == outcome_idx else 0.0) - p) ** 2 for i, p in enumerate(probs)) / len(probs)
        total += err
        count += 1
    return total / count if count else 0.0


def fetch_live_summary(url: str = "https://asianscore.com/api/widget/summary", timeout: int = 15) -> dict:
    """Fetch live fixtures and verifiable SHA-256 ledger summary from AsianScore."""
    req = urllib.request.Request(url, headers={"User-Agent": "asianscore-quant-sdk/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))
