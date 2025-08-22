# Project: Analysis of Berkshire Hathaway's Public Equity Portfolio

[cite_start]**Stage:** Problem Framing & Scoping (Stage 01) [cite: 80]

## [cite_start]Problem Statement [cite: 81]
This project aims to dissect the composition, risk profile, and concentration of Berkshire Hathaway's (BRK) publicly disclosed equity holdings. The goal is to provide a clear, data-driven overview of BRK's investment strategy, answering key questions about its market risk (beta), sector allocation, and reliance on top positions. [cite_start]This analysis will help investors understand the principles behind one of the world's most successful holding companies. [cite: 56, 57]

## [cite_start]Stakeholder & User [cite: 83]
[cite_start]The primary stakeholder is a retail investor who admires Warren Buffett's investment philosophy and wants to apply similar principles to their own portfolio. [cite: 58] They need a concise, understandable analysis to guide their own stock selection and portfolio management decisions. They are not a financial expert but are familiar with basic market concepts.

## [cite_start]Useful Answer & Decision [cite: 85]
[cite_start]The analysis will provide both **descriptive** and **predictive** insights. [cite: 59]

* **Artifact**: A summary report (delivered as a Jupyter Notebook) containing key metrics and visualizations.
* **Metrics**:
    * Weighted Average Portfolio Beta (a measure of systematic risk).
    * Sector concentration percentages.
    * Performance comparison against the S&P 500.
* **Decision**: The stakeholder will use these insights to decide whether to mimic BRK's sector weights, invest in some of the same companies, or adopt a similar risk posture.

## [cite_start]Assumptions & Constraints [cite: 87]
* [cite_start]**Data Availability**: The analysis is based on publicly available holdings data, which may not be fully up-to-date. [cite: 88]
* **Scope**: The analysis is limited to equity holdings and does not include BRK's wholly-owned subsidiaries or cash reserves.
* [cite_start]**Capacity**: Calculations will be performed using standard Python libraries and are not expected to be computationally intensive. [cite: 88]

## [cite_start]Known Unknowns / Risks [cite: 89]
* **Timing Mismatch**: Public filings are delayed, so the current portfolio may differ from the one analyzed.
* **Price Volatility**: Market prices used to value the portfolio are as of a single point in time and are subject to change.

## [cite_start]Repo Plan [cite: 95]
* **/data/**: Stores raw and processed datasets.
* **/src/**: Contains reusable Python utility and cleaning functions.
* **/notebooks/**: Holds notebooks for each stage of the analysis.
* [cite_start]**/docs/**: Contains stakeholder-facing documents like memos. [cite: 96]

---
## Data Storage Section (Added in Stage 5)
* [cite_start]**Folder Structure**: We use `data/raw/` for immutable, originally sourced data and `data/processed/` for cleaned, analysis-ready data. [cite: 347]
* **Formats**: Raw data is saved as **CSV** for its portability. [cite_start]Processed data is saved as **Parquet** for efficient storage and faster read/write operations with typed columns. [cite: 348]
* [cite_start]**Access**: Code reads and writes data using environment variables (`DATA_DIR_RAW`, `DATA_DIR_PROCESSED`) to ensure the code is portable and not hardcoded. [cite: 349]

---
## Cleaning Strategy (Added in Stage 6)
Data cleaning is performed using modular functions stored in `src/cleaning.py`. The primary steps include handling missing values for key financial metrics (e.g., filling with the median) and normalizing skewed data (e.g., market capitalization) for certain analyses. [cite_start]All assumptions, such as the choice of imputation strategy, are documented directly in the analysis notebook. [cite: 166]