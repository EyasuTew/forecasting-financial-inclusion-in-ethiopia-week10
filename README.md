# 10 Academy Week 10 Challenge  
**Forecasting Financial Inclusion in Ethiopia**

**Challenge period**: 28 January 2026 – 03 February 2026  
**Current date**: 31 January 2026  
**Status**: Tasks 1 & 2 completed (Data Exploration, Enrichment & EDA)  
**Interim submission ready**

## Project Goal

Build a forecasting system to track Ethiopia's digital financial transformation, focusing on two core Global Findex indicators:

- **Access** — Account Ownership Rate (% of adults 15+ with an account or mobile money)
- **Usage** — Digital Payment Adoption Rate (% who made/received digital payments)

The system should:
- Analyze historical patterns and event impacts (product launches, policies, infrastructure)
- Forecast progress for 2025–2027
- Present findings through an interactive dashboard

**Key context (2026)**:  
Despite Telebirr reaching ~58.6 million users and total registered digital accounts exceeding 220 million, Global Findex 2025 shows account ownership only increased from 46% (2021) to **49%** (2024) — a mere +3 percentage points.

## Repository Structure

```
ethiopia-fi-forecast/
├── data/
│   ├── raw/
│   │   ├── ethiopia_fi_unified_data.xlsx       # Starter unified dataset
│   │   └── reference_codes.xlsx                # Valid categorical values
│   └── processed/
│       └── ethiopia_fi_enriched_20260131.xlsx  # Enriched dataset (Task 1 output)
├── notebooks/
│   └── task1_task2.ipynb                       # Combined notebook for Tasks 1 & 2
├── reports/
│   └── figures/                                # Exported EDA visualizations
├── src/                                        # (future) reusable Python modules
├── dashboard/
│   └── app.py                                  # (future) Streamlit dashboard
├── data_enrichment_log.md                      # Full documentation of added records
├── requirements.txt                            # Python dependencies
├── README.md                                   # This file
└── .gitignore
```

## Key Findings – Tasks 1 & 2 (31 January 2026)

### Dataset Overview
- Total records: **43**
  - Observations: 30
  - Events: 10
  - Targets: 3
- 34 columns in unified schema (`record_id`, `record_type`, `pillar`, `indicator_code`, `value_numeric`, `observation_date`, `category`, `source_url`, `confidence`, `impact_magnitude`, etc.)
- Temporal coverage (observations): mainly Findex years (2014, 2017, 2021, 2024) + recent 2023–2025 operator/infrastructure data
- Top indicators:
  - `ACC_OWNERSHIP` (6 records)
  - `ACC_FAYDA` (3)
  - `ACC_MM_ACCOUNT`, `ACC_4G_COV`, `USG_P2P_COUNT`, `GEN_GAP_ACC` (2 each)

**Challenge**: Events often lack dedicated `event_date` / `description` columns → using `observation_date` proxy + `category` / `notes` for timeline visualization.

### Enrichment Performed (Task 1)
Five high-value records added to capture latest 2025 reality:

| # | Type        | Pillar | Indicator Code       | Value          | Date       | Source                                      | Confidence | Rationale / Why Useful                              |
|---|-------------|--------|----------------------|----------------|------------|---------------------------------------------|------------|-----------------------------------------------------|
| 1 | observation | Access | ACC_OWNERSHIP        | 49.0           | 2024-12-31 | World Bank Global Findex 2025               | high       | Latest official benchmark – slow progress           |
| 2 | event       | —      | —                    | —              | 2025-12-31 | Ethio Telecom H1 FY2025/26 Report           | high       | Telebirr milestone: 58.61 million users             |
| 3 | observation | Usage  | REG_DIGITAL_ACCOUNTS | 222,100,000    | 2025-03-31 | NBE / Shega Media                           | medium     | Supply-side explosion – explains inactivity issue   |
| 4 | observation | Access | ACC_OWNERSHIP_MALE   | 57.0           | 2024-12-31 | Global Findex 2025                          | high       | Persistent gender gap – important for equity focus  |
| 5 | observation | Access | ACC_OWNERSHIP_FEMALE | 42.0           | 2024-12-31 | Global Findex 2025                          | high       | Persistent gender gap – important for equity focus  |

→ Full documentation with sources, quotes, confidence rationale and collection notes:  
[`data_enrichment_log.md`](./data_enrichment_log.md)

**Output file**: `data/processed/ethiopia_fi_enriched_20260131.xlsx`

### EDA Highlights – Task 2

#### Main Observations
- Account ownership trajectory:  
  2014: 22% → 2017: 35% (+13 pp) → 2021: 46% (+11 pp) → **2024: 49% (+3 pp only)**
- Massive supply-side growth: ~222 million registered digital accounts (2025), but demand-side usage remains low
- Persistent **15 percentage point gender gap** (men 57%, women 42% in 2024)
- P2P transactions dominate; merchant payments, wages, bill pay still marginal

#### Key Insights (minimum 5 required)

1. **Access growth has almost stalled**  
   Only +3 pp between 2021–2024 despite Telebirr (58.6M users) and >220M registered accounts → many inactive / duplicate accounts.

2. **Gender disparity remains large and stable**  
   15 pp gap (men 57%, women 42%) → women continue to be significantly excluded.

3. **Registered accounts ≠ active usage**  
   Supply-side metrics exploded, but Findex demand-side indicators show low activation.

4. **P2P dominance and shallow usage depth**  
   Digital payments mostly person-to-person (commerce/remittances); merchant, wage, bill pay limited → aligns with Ethiopia market nuances.

5. **Significant data limitations**  
   Triennial Findex surveys + irregular supply-side reporting → wide gaps in short-term event impact detection.

6. **Modeling hypothesis**  
   Infrastructure (Fayda digital ID, agent networks, interoperability) and activation enablers likely have larger, longer-lagged effects than standalone product launches.

## How to Run the Analysis (Tasks 1 & 2)

1. Clone the repository
   ```bash
   git clone <your-repository-url>
   cd ethiopia-fi-forecast
   ```

2. Create and activate virtual environment (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate          # Linux/macOS
   # or
   .venv\Scripts\activate             # Windows
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

   Typical content of `requirements.txt`:
   ```
   pandas>=2.0
   numpy
   matplotlib
   seaborn
   openpyxl
   jupyter
   ```

4. Launch Jupyter and open the notebook
   ```bash
   jupyter notebook
   # or
   jupyter lab
   ```
   → Navigate to `notebooks/task1_task2.ipynb`

## Next Steps (Planned – Week 10 Timeline)

- Merge `task-1` and `task-2` branches into `main`
- **Task 3**: Event impact modeling (association matrix from `impact_link` + enriched estimates + comparable evidence)
- **Task 4**: Forecasting Access & Usage 2025–2027 (trend + intervention models, scenarios)
- **Task 5**: Interactive Streamlit dashboard (`dashboard/app.py`)

## References & Data Sources

- Global Findex Database 2025 → https://www.worldbank.org/en/publication/globalfindex
- Ethio Telecom official reports → https://www.ethiotelecom.et
- National Bank of Ethiopia / Shega Media → https://digitalfinance.shega.co
- Challenge starter files: `ethiopia_fi_unified_data.xlsx` & `reference_codes.xlsx`


---

**Last updated**: 31 January 2026
```

Feel free to customize:
- Replace `<your-repository-url>` with the actual GitHub link
- Add screenshots of key plots later (e.g. `![Account Ownership Trend](reports/figures/account_trend.png)`)
- Update when Tasks 3–5 are completed

Let me know if you want to add GitHub badges, a table of contents, contribution section, or make it more visual!



# Tasks 3–5: Event Impact Modeling, Forecasting & Interactive Dashboard

**Completed**: February 2026  
**Current branch status**: `task-5` (merged from task-3 and task-4)

This section documents the implementation and deliverables for the final three tasks of the challenge.

## Task 3 – Event Impact Modeling

**Objective**  
Quantify how catalogued events (product launches, policy changes, infrastructure investments) affect key financial inclusion indicators (primarily Access and Usage).

**Key outputs**

- Event-indicator association matrix (estimated impact in percentage points)
- Heatmap visualization of impacts
- Historical validation (e.g. Telebirr launch May 2021)
- Methodology documentation & limitations

**Implementation notes**

- The starter dataset contained **no usable `impact_link` records** (or linking column was missing → `parent_id` not found).
- Fallback approach: created a **manual/estimated impact matrix** using:
  - Observed pre/post changes from historical data
  - Market nuances (Sheet D)
  - Comparable country evidence (e.g. Kenya M-Pesa long-term effects)
- Conservative estimates applied (product launches down-weighted due to observed stagnation)

**Main files**

- `notebooks/task3_event_impact_modeling.ipynb` → diagnostics, manual matrix, heatmap
- `reports/figures/task3_impact_matrix_estimated.png` → saved heatmap

**Example matrix excerpt** (estimated pp change after lag)

| Event (partial name)     | ACC_OWNERSHIP | ACC_MM_ACCOUNT | USG_DIGITAL_PAYMENT |
|--------------------------|---------------|----------------|---------------------|
| Telebirr                 | +1.2          | +4.8           | —                   |
| M-Pesa                   | —             | +2.5           | —                   |
| Fayda                    | +4.0          | —              | —                   |
| Interoperability         | —             | —              | +6.0                |

## Task 4 – Forecasting Access and Usage (2025–2027)

**Objective**  
Produce point forecasts + uncertainty ranges for:

- **Access**: Account Ownership Rate (`ACC_OWNERSHIP`)
- **Usage**: Digital Payment Adoption Rate (proxied)

with baseline trend continuation and event-augmented scenarios.

**Approach** (given very sparse data: only 4 reliable Findex points)

1. Linear OLS trend fitted on 2014–2024 ownership points
2. Added lagged step interventions from Task 3 manual estimates
3. Three scenarios generated:
   - Baseline (pure trend)
   - With Events (intervention effects)
   - Optimistic / Pessimistic bounds

**Forecast summary (mid-point estimates)**

| Year | Baseline | With Events | Optimistic | Pessimistic |
|------|----------|-------------|------------|-------------|
| 2025 | 50.8%    | 52.6%       | 53.5%      | 49.0%       |
| 2026 | 52.1%    | 55.3%       | 56.8%      | 49.5%       |
| 2027 | 53.4%    | 57.9%       | 59.2%      | 50.0%       |

**Main files**

- `notebooks/task4_forecasting_2025_2027.ipynb` → trend model, intervention addition, scenarios
- `reports/figures/task4_forecast_access.png` → main forecast visualization

**Interpretation highlights**

- Baseline trend alone → ~53% by 2027 (very slow)
- Plausible event effects (Fayda, interoperability, agents) → could reach ~58% by 2027
- Still below aspirational NFIS-II ~60% target → activation remains critical

## Task 5 – Interactive Dashboard

**Objective**  
Create a stakeholder-facing Streamlit dashboard with ≥4 interactive visualizations.

**Features implemented**

- **Overview tab**: key metrics cards (ownership, registered accounts, Telebirr users, gender gap, P2P dominance)
- **Trends tab**: historical ownership line chart + toggleable event annotations
- **Forecasts tab**: interactive scenario selector (baseline / with events / optimistic / pessimistic) + uncertainty bands + adjustable NFIS target line
- **Progress tab**: gauge indicator showing current position vs chosen target + gap metric

**Technology**

- Streamlit + Plotly (interactive charts)
- Hard-coded data for simplicity (can be replaced with CSV/Excel loading later)

**How to run**

```bash
pip install streamlit plotly pandas numpy
streamlit run src/app.py