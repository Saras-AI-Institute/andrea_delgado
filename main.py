#Added this line to fix the error on streamlit for the image
from pathlib import Path
import streamlit as st  # type: ignore[import]
from PIL import Image  # for handling images
import datetime
import pandas as pd  # for data manipulation 
# Install matplotlib
# conda install matplotlib

# Setting the page configuration
st.set_page_config(
    layout="wide", 
    page_title="FitSync",
    page_icon="🏋️‍♂️"
)

# --- Shared on all pages ---
# Display your logo at the top of the app
st.image("/workspaces/andrea_delgado/assets/fitsync_logo_b.png", use_column_width=True)

# Set a title and subtitle with centered alignment
#st.title("Welcome to FitSync!", anchor=None)
#st.subheader("Your personalized fitness journey.", anchor=None)
# --- Logo and Dark/Light Theme Toggle ---

# Load your logo image (ensure the image file is in your directory)
#logo = Image.open("/workspaces/andrea_delgado/assets/fitsync_logo_b.png")
logo_path = Path(__file__).parent / "assets" / "fitsync_logo_b.png"
st.image(str(logo_path), use_container_width=True)

# Add the logo at the top
#st.image(logo, width=170)

# Shared on all Pages
#st.logo("/workspaces/andrea_delgado/assets/fitsync_logo_b.png")
st.sidebar.text("Made with ❤️ by Andie")


# Initialize session state for theme toggle
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Create a button in the sidebar to toggle the theme
theme_toggle = st.sidebar.radio(
    "Theme", 
    ["Light", "Dark"], 
    index=0 if not st.session_state.dark_mode else 1,
    on_change=toggle_theme
)

# Set CSS styles based on the theme
theme_css = """
<style>
body {
    background-color: #2a2a2a;
    color: white;
}
</style>
""" if st.session_state.dark_mode else """
<style>
body {
    background-color: white;
    color: black;
}
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<h1 style='text-align: center; font-size: 2.5em;'>✨ Welcome to FitSync ✨</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Your Personal Health Analytics Dashboard 🏋️</h2>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'><button style='font-size: 1.2em;'>Get Started</button></div>", unsafe_allow_html=True)

# --- Dashboard Metrics/Cards Section ---
# Use columns for metrics
col1, col2, col3 = st.columns(3)

# Add metric boxes or dashboard-style cards
with col1:
    st.metric("➡️ Steps Today", "5,432")
with col2:
    st.metric("🩵 Water Intake", "2.5 L")
with col3:
    st.metric("🔥 Calories Burned", "345 cal")

# --- What FitSync Does Section ---
with st.container():
    st.markdown("<h3 style='text-align: center;'>What FitSync Does</h3>", unsafe_allow_html=True)
    st.write("""
    FitSync is your companion for health analytics. It helps track your daily activities, analyze trends, and keep your health goals on track.
    """)

