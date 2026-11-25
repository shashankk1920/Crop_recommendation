import streamlit as st

from utils.styles import load_css
from utils.ui import (
    show_sidebar,
    show_header,
    show_dashboard_cards,
    show_footer

)

from utils.predictor import prediction_form

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="🌾 Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# ---------------- CSS ----------------
load_css()

# ---------------- Sidebar ----------------
show_sidebar()

# ---------------- Header ----------------
show_header()

# ---------------- Dashboard ----------------
show_dashboard_cards()

st.divider()

# ---------------- Prediction Form ----------------
prediction_form()

# ---------------- Footer ----------------
st.divider()

show_footer()
