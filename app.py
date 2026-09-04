import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("data/processed/unemployment_cleaned.csv", parse_dates=['Date'])

st.set_page_config(page_title="India Unemployment Dashboard", layout="wide")

st.title("India Unemployment Analysis Dashboard")
st.markdown("Exploring unemployment trends in India, May 2019 – June 2020, with focus on the COVID-19 impact.")

# Sidebar filters
st.sidebar.header("Filters")
selected_region = st.sidebar.selectbox("Select a State/Region", options=["All India"] + sorted(df['Region'].unique().tolist()))
selected_area = st.sidebar.multiselect("Select Area Type", options=df['Area'].unique().tolist(), default=df['Area'].unique().tolist())

# Filter data based on selections
filtered = df[df['Area'].isin(selected_area)]
if selected_region != "All India":
    filtered = filtered[filtered['Region'] == selected_region]

# Key stats
pre_covid = filtered[filtered['Date'] < '2020-03-01']
covid_period = filtered[filtered['Date'] >= '2020-03-01']

col1, col2, col3 = st.columns(3)
col1.metric("Pre-COVID Avg", f"{pre_covid['Estimated Unemployment Rate (%)'].mean():.2f}%")
col2.metric("During COVID Avg", f"{covid_period['Estimated Unemployment Rate (%)'].mean():.2f}%")
col3.metric("Change", f"{covid_period['Estimated Unemployment Rate (%)'].mean() - pre_covid['Estimated Unemployment Rate (%)'].mean():.2f} pp")

# Trend chart
st.subheader(f"Unemployment Trend: {selected_region}")
trend = filtered.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(trend.index, trend.values, marker='o', color='steelblue')
ax.set_xlabel("Date")
ax.set_ylabel("Unemployment Rate (%)")
ax.grid(True, alpha=0.3)
st.pyplot(fig)

st.markdown("---")
st.caption("Data source: Kaggle - Unemployment in India dataset")