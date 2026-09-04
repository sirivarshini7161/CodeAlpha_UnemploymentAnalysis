# Unemployment Analysis in India (COVID-19 Impact)
🔗 **Live Dashboard:** https://unemployment-analysis-python-a6pqrzeesh4hpt7nojek47.streamlit.app
## Problem Statement
Analyze unemployment rate data across Indian states to understand trends over time, with a specific focus on the impact of the COVID-19 lockdown (2020) on employment.

## Objective
- Explore how unemployment changed in India from May 2019 to June 2020
- Quantify the impact of COVID-19 on unemployment at a national and state level
- Compare Rural vs Urban unemployment trends
- Identify which states were hit hardest
- Present findings through visualizations and an interactive dashboard

## Dataset
Source: [Unemployment in India](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india) (Kaggle)
- 768 rows, 7 columns before cleaning
- Covers 28 Indian states/UTs, May 2019 – June 2020
- Fields: Region, Date, Estimated Unemployment Rate (%), Estimated Employed, Estimated Labour Participation Rate (%), Area (Rural/Urban)

## Technologies Used
- Python 3.10
- Pandas, NumPy — data manipulation
- Matplotlib, Seaborn — visualization
- Streamlit — interactive dashboard
- Jupyter Notebook — analysis environment

## Project Architecture
```
unemployment-analysis-python/
├── data/
│   ├── raw/              # original dataset
│   └── processed/        # cleaned dataset
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   └── 02_eda.ipynb
├── visualizations/        # exported charts
├── app.py                 # Streamlit dashboard
├── requirements.txt
├── README.md
└── .gitignore
```
## Data Cleaning
- Removed 28 fully blank rows (no data in any column)
- Stripped inconsistent leading/trailing whitespace from column headers and text values (e.g., `' Monthly'` vs `'Monthly'` were being treated as different categories)
- Dropped the `Frequency` column (constant value "Monthly" across all rows — no analytical value)
- Converted `Date` from text to proper datetime format
- Verified no duplicate rows
- Verified value ranges were plausible; confirmed extreme unemployment values (up to 76.74%) were genuine COVID-lockdown effects, not data errors

## Exploratory Data Analysis
- National unemployment trend over time
- Pre-COVID vs During-COVID comparison
- Rural vs Urban trend comparison
- State-wise ranking of COVID impact
- Distribution analysis (box plot)
- Correlation check between Labour Participation Rate and Unemployment Rate

## Key Insights
- **National unemployment nearly doubled during COVID**: average rate rose from 9.51% (pre-COVID) to 17.77% (Mar–Jun 2020), an increase of 8.26 percentage points (86.9% relative increase)
- **Urban areas were hit harder than Rural areas**, peaking at ~28% (Urban, May 2020) vs ~22% (Rural, April 2020)
- **Puducherry, Tamil Nadu, and Jharkhand** saw the largest increases in unemployment
- **No linear correlation** (r ≈ 0.00) was found between Labour Participation Rate and Unemployment Rate — these metrics moved independently during this period

## Business/Real-World Impact
These findings could inform targeted economic relief: states and urban centers that saw the sharpest unemployment spikes may have needed more aggressive, timely support measures than the national average would suggest.

## Interactive Dashboard
🔗 **Live Dashboard:** https://unemployment-analysis-python-a6pqrzeesh4hpt7nojek47.streamlit.app
An interactive Streamlit dashboard is included (`app.py`), allowing users to filter by state and area type (Rural/Urban) and view live-updating statistics and trend charts.

## Installation
```bash
   git clone https://github.com/sirivarshini7161/unemployment-analysis-python.git
cd unemployment-analysis-python
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## How to Run
- Notebooks: open `notebooks/01_data_understanding.ipynb` and `notebooks/02_eda.ipynb` in VS Code or Jupyter
- Dashboard: `streamlit run app.py`

## Future Improvements
- Extend analysis with more recent data (post-June 2020) to assess recovery
- Add a simple forecasting model
- Add authentication or caching for faster dashboard load times

## Author
Sirivarshini — B.Tech Data Science Student, CodeAlpha Data Science Internship