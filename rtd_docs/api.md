# API Reference

All symbols are exported at the top level of `asianscore_quant` and implemented in `asianscore_quant.math_models` using only the Python standard library.

Interactive browser equivalents for these models are available on [AsianScore Quantitative Tools](https://asianscore.com/tools.html).

## `devig_multiplicative(decimal_odds)`

Removes bookmaker overround proportionally from a sequence of decimal odds.

```python
devig_multiplicative(decimal_odds: Sequence[float]) -> List[float]
```

- **Parameters**:
  - `decimal_odds`: Non-empty sequence of decimal odds where every value is `> 1.0`.
- **Returns**: Normalized fair probability list summing to `1.0`.
- **Raises**: `ValueError` if `decimal_odds` is empty or contains any odds `<= 1.0`.

## `devig_power(decimal_odds, tol=1e-9, max_iter=80)`

Solves `sum((1 / o_i)^k) = 1` via bisection over `k in [0.2, 5.0]` to account for favorite-longshot bias.

```python
devig_power(decimal_odds: Sequence[float], tol: float = 1e-9, max_iter: int = 80) -> List[float]
```

- **Parameters**:
  - `decimal_odds`: Non-empty sequence of decimal odds (`> 1.0`).
  - `tol`: Bisection stopping tolerance on `abs(sum(p_i^k) - 1)`.
  - `max_iter`: Maximum bisection iterations.
- **Returns**: Normalized fair probability list summing to `1.0`.
- **Raises**: `ValueError` if `decimal_odds` is empty or contains any odds `<= 1.0`.

## `kelly_fraction(fair_prob, decimal_odds, scale=0.25)`

Computes the fractional Kelly criterion bankroll stake.

```python
kelly_fraction(fair_prob: float, decimal_odds: float, scale: float = 0.25) -> float
```

- **Parameters**:
  - `fair_prob`: Estimated true probability in `(0.0, 1.0)`.
  - `decimal_odds`: Available decimal odds (`> 1.0`).
  - `scale`: Fractional Kelly multiplier (defaults to `0.25`, quarter-Kelly).
- **Returns**: Recommended stake fraction (`>= 0.0`). Returns `0.0` when edge is negative or inputs are out of range.

## `dixon_coles_probs(lambda_home, lambda_away, rho=-0.05, max_goals=10)`

Computes 1X2 and Over 2.5 Goals probabilities from a Dixon-Coles low-score correlation adjusted bivariate Poisson score matrix.

```python
dixon_coles_probs(
    lambda_home: float,
    lambda_away: float,
    rho: float = -0.05,
    max_goals: int = 10,
) -> Dict[str, float]
```

- **Parameters**:
  - `lambda_home`: Expected goals for the home side.
  - `lambda_away`: Expected goals for the away side.
  - `rho`: Low-score correlation parameter applied to `(0,0)`, `(0,1)`, `(1,0)`, and `(1,1)` scorelines.
  - `max_goals`: Goal truncation bound per side (default `10`).
- **Returns**: Dictionary with keys `"home"`, `"draw"`, `"away"`, and `"over_2_5"`, rounded to 6 decimal places.

## `brier_score(predictions)`

Computes the multi-class Brier score (mean squared error across outcome probabilities).

```python
brier_score(predictions: Iterable[Tuple[Sequence[float], int]]) -> float
```

- **Parameters**:
  - `predictions`: Iterable of `(probs, outcome_idx)` pairs, where `probs` is the predicted probability vector and `outcome_idx` is the zero-based index of the realized outcome.
- **Returns**: Mean squared error across all predictions (`0.0` if empty).

## `fetch_live_summary(url="https://asianscore.com/api/widget/summary", timeout=15)`

Fetches live fixture probabilities and verifiable SHA-256 ledger summary statistics from [AsianScore](https://asianscore.com/).

```python
fetch_live_summary(
    url: str = "https://asianscore.com/api/widget/summary",
    timeout: int = 15,
) -> dict
```

- **Parameters**:
  - `url`: Summary JSON endpoint (CORS-enabled, no API key required).
  - `timeout`: Request timeout in seconds.
- **Returns**: Parsed JSON dictionary containing `ledger` metrics and active `matches`.
