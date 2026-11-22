# AsianScore Quant SDK (`asianscore-quant`)

[![PyPI version](https://img.shields.io/pypi/v/asianscore-quant)](https://pypi.org/project/asianscore-quant/)
[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24441036.svg)](https://doi.org/10.5281/zenodo.24441036)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/AIYIXIU/asianscore-quant-sdk/blob/main/LICENSE)

Zero-dependency Python sports quantitative toolkit implementing the exact mathematical primitives powering [AsianScore](https://asianscore.com/):

- **Odds De-Vigging:** Multiplicative & Power-method fair probability solvers (`devig_multiplicative`, `devig_power`)
- **Bankroll Management:** Fractional Kelly Criterion (`kelly_fraction`)
- **Football xG Modeling:** Dixon-Coles low-score correlation bivariate Poisson grid (`dixon_coles_probs`)
- **Calibration Auditing:** Multi-class Brier score (`brier_score`)
- **Live Open Feed Client:** `fetch_live_summary()` querying `https://asianscore.com/api/widget/summary` (CORS-enabled, no API key required)

## Installation

```bash
pip install asianscore-quant
```

## Quick Start

```python
from asianscore_quant import devig_power, dixon_coles_probs, kelly_fraction, brier_score

fair = devig_power([2.10, 3.40, 3.60])
grid = dixon_coles_probs(1.62, 1.18, rho=-0.08)
stake = kelly_fraction(prob=0.52, decimal_odds=2.10, fraction=0.25)
score = brier_score([0.55, 0.25, 0.20], actual_index=0)
```

## Open Platform & Ecosystem

- **Official Platform:** https://asianscore.com/
- **Interactive Web Calculators:** https://asianscore.com/tools.html
- **SHA-256 Verifiable AI Prediction Ledger:** https://asianscore.com/models.html#ledger
- **Zenodo Academic Dataset (CERN DOI):** https://doi.org/10.5281/zenodo.24441036
- **Docs (GitHub Pages):** https://aiyixiu.github.io/asianscore-quant-sdk/
- **Official Go Package (`pkg.go.dev`):** https://pkg.go.dev/github.com/AIYIXIU/asianscore-go
- **Embeddable Live Widget:** https://aiyixiu.github.io/asianscore-live-widget/

## Verification

```bash
python3 -m unittest tests/test_quant.py
```

## License

MIT
