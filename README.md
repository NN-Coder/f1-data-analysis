# F1 Data Analysis: Constructor Racecraft Performance

This project analyzes historical Formula 1 race result data to evaluate constructor-level racecraft through **Average Positions Gained (APG)**, defined as:

`APG = grid position - final position`

A higher APG indicates that, on average, a team improves more positions between the race start and finish.

## Project Goals

- Quantify which constructors gain the most positions during races.
- Compare APG against sample size (total race entries) to highlight variance in small datasets.
- Provide both static and interactive visualizations for exploratory analysis.

## Repository Structure

```text
.
├── data/
│   ├── constructors.csv
│   └── results.csv
├── scripts/
│   ├── main.py
│   ├── scatter-plot.py
│   └── interactive-scatter-plot.py
├── Dockerfile
└── requirements.txt
```

## Data Sources

- `constructors.csv` and `results.csv` were acquired from the Kaggle dataset:  
  https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020

## Analysis Walkthrough

- Presentation with methodology and process:  
  https://docs.google.com/presentation/d/1bZhT_yq7-mdMf9Ao8VaFRqklGW-47c8zOK8FQtB8lGk/edit?usp=sharing

## Scripts

- `scripts/main.py`  
  Core APG analysis with console output and a bar chart of top teams.

- `scripts/scatter-plot.py`  
  Static scatter plot showing APG vs total entries (log-scaled x-axis).

- `scripts/interactive-scatter-plot.py`  
  Interactive Plotly scatter plot for deeper exploratory analysis.

## How to Run

### Option 1: Local Python Environment

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the primary analysis:
   ```bash
   python scripts/main.py
   ```
3. Run visualization scripts:
   ```bash
   python scripts/scatter-plot.py
   python scripts/interactive-scatter-plot.py
   ```

### Option 2: Docker

Build the image:

```bash
docker build -t f1-data-analysis .
```

Run the default analysis script:

```bash
docker run --rm -it -v "$(pwd):/app" f1-data-analysis
```

Run specific scripts:

```bash
docker run --rm -it -v "$(pwd):/app" f1-data-analysis python scripts/scatter-plot.py
docker run --rm -it -v "$(pwd):/app" f1-data-analysis python scripts/interactive-scatter-plot.py
```

## Methodology Summary

1. Load race results and keep only constructor ID, grid position, and final classified position.
2. Compute per-race positions gained for each constructor entry.
3. Aggregate APG by constructor and compute total race entries.
4. Merge constructor metadata for readable team names.
5. Apply entry-count thresholds where appropriate to reduce small-sample distortion.
6. Compare central trend and variance through ranked tables and scatter plots.

## Key Interpretation Notes

- Teams with very few race entries can produce extreme APG values that are not stable estimates.
- Entry thresholds and log-scaled visualizations are used to make comparisons more statistically meaningful.
- APG captures race-day progression, not overall team performance across qualifying, reliability, or points systems.
