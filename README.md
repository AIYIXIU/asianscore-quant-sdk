# AsianScore Quant SDK

Zero-dependency Python sports quantitative toolkit implementing the exact mathematical primitives powering [AsianScore](https://asianscore.com/):

- **Odds Devigging:** Multiplicative & Power-method fair probability solvers (`devig_multiplicative`, `devig_power`)
- **Bankroll Management:** Fractional Kelly Criterion (`kelly_fraction`)
- **Football xG Modeling:** Dixon-Coles low-score correlation bivariate Poisson grid (`dixon_coles_probs`)
- **Calibration Auditing:** Multi-class Brier score (`brier_score`)
- **Live Open Feed Client:** `fetch_live_summary()` querying `https://asianscore.com/api/widget/summary` (CORS-enabled, no API key required)

### Links

- **Official Platform:** https://asianscore.com/
- **Interactive Web Calculators:** https://asianscore.com/tools.html
- **SHA-256 Verifiable AI Prediction Ledger:** https://asianscore.com/ai.html
- **Docs (GitHub Pages):** https://aiyixiu.github.io/asianscore-quant-sdk/
- **Open Dataset (CC BY 4.0):** https://github.com/AIYIXIU/asianscore-xg-ledger-dataset
- **Embeddable Live Widget:** https://github.com/AIYIXIU/asianscore-live-widget

### Verification

```bash
python3 -m unittest tests/test_quant.py
```

## License

MIT
