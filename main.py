import streamlit as st
from modules.processor import process_data
import pandas as pd

# Set the page configuration for a wide layout and set the page title
st.set_page_config(layout="wide", page_title="FitSync")

# Title of the dashboard
st.title("FitSync - Personal Health Analytics")

# Load the data using process_data
df = process_data()

# Sidebar for Filters
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Filter the DataFrame based on the selected time range
if time_range == "Last 7 Days":
    df = df[df['Date'] >= (df['Date'].max() - pd.Timedelta(days=7))]
elif time_range == "Last 30 Days":
    df = df[df['Date'] >= (df['Date'].max() - pd.Timedelta(days=30))]
# If "All Time" is selected, we do not change df

# Calculate the required metrics from the filtered DataFrame
daily_average_steps = df['Steps'].mean()
daily_average_sleep = df['Sleep_Hours'].mean()
daily_average_recovery_score = df['Recovery_Score'].mean()

# Create a 3-column layout for metrics
col1, col2, col3 = st.columns(3)

# Display the metrics in respective columns
with col1:
    st.metric(label="Average Steps", value=f"{daily_average_steps:.0f}", delta=None)

with col2:
    st.metric(label="Average Sleep Hours", value=f"{daily_average_sleep:.1f}", delta=None)

with col3:
    st.metric(label="Average Recovery Score", value=f"{daily_average_recovery_score:.1f}", delta=None)

# Move the data processing and display the DataFrame and visuals after metrics
# Processed data and visualizations
st.dataframe(df)
st.line_chart(df.set_index('Date')['Recovery_Score'])

# Use a multiselect widget for selecting columns
columns_to_show = st.multiselect(
    "Select columns to display:", list(df.columns), default=list(df.columns)
)

# Display filtered data
st.dataframe(df[columns_to_show])

# Additional custom widgets or sections can be added here to enhance the dashboard