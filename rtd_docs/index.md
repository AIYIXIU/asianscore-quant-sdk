# AsianScore Quant SDK

`asianscore-quant` is a zero-dependency Python sports quantitative toolkit implementing the mathematical primitives behind [AsianScore](https://asianscore.com/).

- **Odds De-Vigging**: Proportional multiplicative and bisection power-method fair probability solvers (`devig_multiplicative`, `devig_power`).
- **Football xG Modeling**: Dixon-Coles low-score correlation bivariate Poisson 1X2 and Over/Under 2.5 probabilities (`dixon_coles_probs`).
- **Bankroll Management**: Fractional Kelly criterion sizing (`kelly_fraction`).
- **Calibration Auditing**: Multi-class Brier score evaluation (`brier_score`).
- **Live Open Feed Client**: Zero-auth JSON client for live fixtures and ledger snapshots (`fetch_live_summary`).

## Installation

```bash
pip install asianscore-quant
```

Or install directly from source:

```bash
git clone https://github.com/AIYIXIU/asianscore-quant-sdk.git
cd asianscore-quant-sdk
pip install .
```

## Quick Start

```python
from asianscore_quant import (
    devig_power,
    dixon_coles_probs,
    kelly_fraction,
    brier_score,
)

# 1. Remove bookmaker overround via power method
fair_probs = devig_power([1.95, 3.50, 4.10])

# 2. Compute Dixon-Coles 1X2 & O/U 2.5 probabilities from expected goals
probs = dixon_coles_probs(lambda_home=1.65, lambda_away=1.05, rho=-0.05)

# 3. Calculate quarter-Kelly stake fraction
stake = kelly_fraction(fair_prob=0.55, decimal_odds=2.0, scale=0.25)

# 4. Evaluate probability calibration with multi-class Brier score
score = brier_score([([0.70, 0.20, 0.10], 0)])
```

## Interactive Tools & Ecosystem

- [AsianScore Platform](https://asianscore.com/)
- [Interactive Web Calculators (De-Vig, Kelly, Dixon-Coles)](https://asianscore.com/tools.html)
- [SHA-256 Verifiable AI Prediction Ledger](https://asianscore.com/models.html#ledger)
- [PyPI Package (`asianscore-quant`)](https://pypi.org/project/asianscore-quant/)
- [Zenodo Open Dataset (DOI 10.5281/zenodo.24441036)](https://doi.org/10.5281/zenodo.24441036)
- [Hugging Face Dataset (`asianscore/football-nba-xg-prediction-ledger`)](https://huggingface.co/datasets/asianscore/football-nba-xg-prediction-ledger)
- [Official Go SDK (`pkg.go.dev`)](https://pkg.go.dev/github.com/AIYIXIU/asianscore-go)
