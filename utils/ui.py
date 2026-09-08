import streamlit as st

def show_sidebar():

    st.sidebar.title("🌿 Crop AI")

    st.sidebar.markdown("---")

    st.sidebar.info("""

### About

This AI recommends the best crop based on:

- 🌱 Nitrogen
- 🧪 Phosphorus
- 🪴 Potassium
- 🌡 Temperature
- 💧 Humidity
- ⚗ Soil pH
- 🌧 Rainfall

### Built With

- Python
- Streamlit
- Scikit-Learn
- Random Forest

""")


def show_header():

    st.markdown("""

<div class="big-title">
🌾 Crop Recommendation System
</div>

<div class="sub-title">
AI Powered Smart Farming Assistant<br>
Get the best crop recommendation using Soil & Weather Data
</div>

""", unsafe_allow_html=True)


def show_dashboard_cards():

    c1,c2,c3,c4=st.columns(4)

    cards=[
        ("Accuracy","98%"),
        ("Crops","22+"),
        ("Model","Random Forest"),
        ("Prediction","Instant")
    ]

    for col,(title,value) in zip([c1,c2,c3,c4],cards):

        with col:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">{title}</div>
                <div class="metric-value">{value}</div>
            </div>
            """,unsafe_allow_html=True)


def show_footer():

    st.markdown("""

<div class="footer">


Python • Streamlit • Scikit-Learn • Random Forest

</div>

""",unsafe_allow_html=True)