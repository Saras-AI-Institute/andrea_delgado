import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Set the page configuration for a wide layout and set the page title
st.set_page_config(layout="wide", page_title="Trends & Insights")

# Title of the page
st.title("Trends & Insights")

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
    filtered_df = df[df['Date'] >= (df['Date'].max() - pd.Timedelta(days=7))]
elif time_range == "Last 30 Days":
    filtered_df = df[df['Date'] >= (df['Date'].max() - pd.Timedelta(days=30))]
else:
    filtered_df = df

# Show summary statistics for filtered data
st.subheader("Summary Statistics")
summary_stats = filtered_df[['Recovery_Score', 'Sleep_Hours', 'Steps', 'Calories_Burned']].agg(['mean', 'min', 'max'])
st.dataframe(summary_stats)

# Line chart for average Recovery Score month-wise
st.subheader("Average Recovery Score by Month")
filtered_df['Month'] = filtered_df['Date'].dt.to_period('M').astype(str)
monthly_avg_recovery = filtered_df.groupby('Month')['Recovery_Score'].mean().reset_index()
fig1 = px.line(monthly_avg_recovery, x='Month', y='Recovery_Score', title='Monthly Average Recovery Score')
st.plotly_chart(fig1, use_container_width=True)

# Histograms for distribution of variables
st.subheader("Distributions")
col1, col2 = st.columns(2)

with col1:
    fig2 = px.histogram(filtered_df, x='Steps', nbins=20, title='Distribution of Steps')
    st.plotly_chart(fig2, use_container_width=True)
    fig3 = px.histogram(filtered_df, x='Recovery_Score', nbins=20, title='Distribution of Recovery Score')
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    fig4 = px.histogram(filtered_df, x='Calories_Burned', nbins=20, title='Distribution of Calories Burned')
    st.plotly_chart(fig4, use_container_width=True)
    fig5 = px.histogram(filtered_df, x='Sleep_Hours', nbins=20, title='Distribution of Sleep Hours')
    st.plotly_chart(fig5, use_container_width=True)