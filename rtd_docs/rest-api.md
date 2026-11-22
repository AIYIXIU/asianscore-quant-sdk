# Public REST API Reference

[AsianScore](https://asianscore.com/) exposes free, keyless, CORS-enabled HTTPS JSON endpoints for live football and NBA scores, pre-kickoff SHA-256 verifiable prediction ledger snapshots, model calibration metrics, and match previews.

- **Base URL:** `https://asianscore.com`
- **Authentication:** None required (public read-only endpoints)
- **Protocol:** HTTPS (`TLS 1.3`, HTTP/2)
- **CORS:** Enabled (`Access-Control-Allow-Origin: *`)
- **Format:** `application/json; charset=utf-8`

---

## Endpoints Overview

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/widget/summary` | `GET` | Compact summary of live/upcoming football & NBA matches plus aggregate ledger Brier score & hit rate |
| `/api/ledger` | `GET` | Full verifiable SHA-256 pre-match prediction ledger (`accuracy`, `byLeague`, `recentSettled`, `upcomingLocked`) |
| `/api/scores` | `GET` | Live & upcoming scoreboard feed across 30+ football leagues and NBA with odds and model score predictions |
| `/api/articles` | `GET` | Latest tactical previews and post-match analytical columns |
| `/embed.js` | `GET` | Zero-dependency embeddable scoreboard script |

---

## 1. `GET /api/widget/summary`

Returns the compact scoreboard and aggregate model calibration metrics used by the [`asianscore-widget`](https://www.npmjs.com/package/asianscore-widget) web component and Go/Python/Ruby SDKs.

### Example Request

```bash
curl -s https://asianscore.com/api/widget/summary
```

### Example Response

```json
{
  "brand": "亚分体育 AsianScore",
  "ledger": {
    "avgBrier": 0.1783,
    "hitRatePct": 56.92,
    "hits": 144,
    "settled": 253,
    "totalLocked": 394
  },
  "matches": [
    {
      "id": "espn-eng.1-401878755",
      "league": "英超",
      "homeTeam": "利物浦",
      "awayTeam": "曼联",
      "homeScore": 0,
      "awayScore": 0,
      "kickoff": "2026-11-23 00:30",
      "state": "pre",
      "topLabel": "利物浦 胜",
      "topProbPct": 60,
      "url": "https://asianscore.com/match/espn-eng.1-401878755.html"
    }
  ]
}
```

---

## 2. `GET /api/ledger`

Returns the tamper-evident pre-match prediction ledger. Predictions are locked 8–10 minutes prior to kickoff with a deterministic SHA-256 input fingerprint and settled against official final scores using multi-class Brier score.

### Example Request

```bash
curl -s https://asianscore.com/api/ledger
```

### Top-Level Fields

| Field | Type | Description |
| --- | --- | --- |
| `schemaVersion` | string | Ledger schema version |
| `generatedAt` | string (ISO-8601) | Snapshot generation timestamp |
| `lockRule` | string | Pre-kickoff freeze rule description |
| `accuracy` | object | Aggregate `averageBrierScore`, `hitRatePct`, `sampleSize`, `correct`, `totalLocked`, `pendingCount` |
| `byLeague` | array/object | Calibration breakdown segmented by league |
| `recentSettled` | array | Settled matches with pre-kickoff probabilities, final score, and Brier score |
| `upcomingLocked` | array | Upcoming matches whose probabilities are already frozen with SHA-256 hash |

---

## 3. `GET /api/scores`

Returns live and upcoming match entries with league filters, market odds, and Dixon-Coles predicted scorelines.

### Example Request

```bash
curl -s https://asianscore.com/api/scores
```

### Match Object Fields

`id`, `sourceEventId`, `leagueCode`, `kickoffAt`, `league`, `day`, `time`, `home`, `away`, `homeZh`, `awayZh`, `venue`, `status`, `liveMin`, `sport`, `oddsHome`, `oddsDraw`, `oddsAway`, `oddsProvider`, `predictedScore`, `predH`, `predA`.

---

## Official SDKs & Open Data Mirrors

- **Python (`asianscore-quant`):** `pip install asianscore-quant` — [PyPI](https://pypi.org/project/asianscore-quant/)
- **Go (`asianscore-go`):** `go get github.com/AIYIXIU/asianscore-go` — [pkg.go.dev](https://pkg.go.dev/github.com/AIYIXIU/asianscore-go)
- **Ruby (`asianscore_quant`):** `gem install asianscore_quant` — [RubyGems](https://rubygems.org/gems/asianscore_quant)
- **JavaScript / Web Component (`asianscore-widget`):** `npm install asianscore-widget` — [npm](https://www.npmjs.com/package/asianscore-widget) · [jsDelivr CDN](https://cdn.jsdelivr.net/npm/asianscore-widget@1.0.0/asianscore-widget.js)
- **Archival Datasets:** [Zenodo DOI 10.5281/zenodo.24441036](https://doi.org/10.5281/zenodo.24441036) · [Hugging Face Dataset](https://huggingface.co/datasets/asianscore/football-nba-xg-prediction-ledger) · [Kaggle Dataset](https://www.kaggle.com/datasets/asianscore/asianscore-football-and-nba-xg-prediction-ledger)
- **Live Platform:** [https://asianscore.com/](https://asianscore.com/) · [Live Scores](https://asianscore.com/scores.html) · [Prediction Ledger](https://asianscore.com/models.html) · [Quant Tools](https://asianscore.com/tools.html)
