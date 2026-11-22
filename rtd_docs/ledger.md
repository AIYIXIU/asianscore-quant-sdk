# Verifiable Ledger & Open Ecosystem

AsianScore publishes pre-match Football and NBA xG probabilities with cryptographic SHA-256 commitments before kickoff so calibration claims can be independently audited after settlement.

## Live Audit & Interactive Tools

- **Platform Home**: [https://asianscore.com/](https://asianscore.com/)
- **SHA-256 Verifiable AI Prediction Ledger**: [https://asianscore.com/models.html#ledger](https://asianscore.com/models.html#ledger)
- **Interactive Web Calculators**: [https://asianscore.com/tools.html](https://asianscore.com/tools.html)

## Fetching Live Summary Data in Python

```python
from asianscore_quant import fetch_live_summary

summary = fetch_live_summary()
ledger = summary.get("ledger", {})
print(
    f"Settled: {ledger.get('settled')} | "
    f"Avg Brier: {ledger.get('avgBrier')} | "
    f"Hit Rate: {ledger.get('hitRatePct')}%"
)
```

## Datasets & Cross-Language Packages

| Resource | Link |
| --- | --- |
| PyPI Python SDK (`asianscore-quant`) | [https://pypi.org/project/asianscore-quant/](https://pypi.org/project/asianscore-quant/) |
| Official Go SDK (`pkg.go.dev`) | [https://pkg.go.dev/github.com/AIYIXIU/asianscore-go](https://pkg.go.dev/github.com/AIYIXIU/asianscore-go) |
| Zenodo Academic Dataset (CERN DOI) | [https://doi.org/10.5281/zenodo.24441036](https://doi.org/10.5281/zenodo.24441036) |
| Hugging Face Dataset | [https://huggingface.co/datasets/asianscore/football-nba-xg-prediction-ledger](https://huggingface.co/datasets/asianscore/football-nba-xg-prediction-ledger) |
