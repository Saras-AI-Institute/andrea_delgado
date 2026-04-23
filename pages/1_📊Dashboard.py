import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set the page configuration for a wide layout and set the page title
st.set_page_config(layout="wide", page_title="FitSync", page_icon="📊")

# Tpip list | grep streamlitpip list | grep streamlititle of the dashboard
st.title("FitSync - Personal Health Analytics")

# To optimize performance, we can cache the data loading function
#@st.cache_data

# Load the data using process_data
#df = process_data()

# Cache the data loading step so Streamlit does not recalculate it every rerun
@st.cache_data
def load_data():
    return process_data()

# Call the cached function
df = load_data()

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

# Calculate the required metrics from the filtered DataFrame
daily_average_steps = filtered_df['Steps'].mean()
daily_average_sleep = filtered_df['Sleep_Hours'].mean()
daily_average_recovery_score = filtered_df['Recovery_Score'].mean()

# Create a 3-column layout for metrics
col1, col2, col3 = st.columns(3)

# Display the metrics in respective columns
with col1:
    st.metric(label="Average Steps", value=f"{daily_average_steps:.0f}", delta=None)

with col2:
    st.metric(label="Average Sleep Hours", value=f"{daily_average_sleep:.1f}", delta=None)

with col3:
    st.metric(label="Average Recovery Score", value=f"{daily_average_recovery_score:.1f}", delta=None)

# Below metrics, create two columns for dual charts
col4, col5 = st.columns(2)

with col4:
    st.subheader("Recovery Score & Sleep Trend")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Recovery_Score'], mode='lines', name='Recovery Score'))
    fig1.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Sleep_Hours'], mode='lines', name='Sleep Hours'))
    fig1.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    st.subheader("Recovery Score vs Daily Steps")
    fig2 = px.scatter(filtered_df, x="Steps", y="Recovery_Score", color="Sleep_Hours")
    fig2.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig2, use_container_width=True)

# Another set of columns below for different charts
col6, col7 = st.columns(2)

with col6:
    st.subheader("Recovery Score vs Resting Heart Rate")
    fig3 = px.scatter(filtered_df, x="Heart_Rate_bpm", y="Recovery_Score")
    fig3.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig3, use_container_width=True)

with col7:
    st.subheader("Daily Calories Burned Trend")
    fig4 = px.line(filtered_df, x="Date", y="Calories_Burned")
    fig4.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig4, use_container_width=True)

# Remove unnecessary data frame display and chart 
# st.dataframe(df)
# st.line_chart(df.set_index('Date')['Recovery_Score'])

# Additional custom widgets or sections can be added here to enhance the dashboard