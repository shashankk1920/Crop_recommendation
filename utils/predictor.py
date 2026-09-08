import streamlit as st
import numpy as np
import joblib


model = joblib.load("crop_model.pkl")


def prediction_form():

    left,right=st.columns(2)

    with left:

        N=st.number_input("🌱 Nitrogen (N)",min_value=0,value=90)

        K=st.number_input("🪴 Potassium (K)",min_value=0,value=43)

        humidity=st.number_input("💧 Humidity (%)",value=80.0)

        rainfall=st.number_input("🌧 Rainfall (mm)",value=200.0)

    with right:

        P=st.number_input("🧪 Phosphorus (P)",min_value=0,value=42)

        temperature=st.number_input("🌡 Temperature (°C)",value=25.0)

        ph=st.number_input("⚗ Soil pH",value=6.5)

    st.write("")

    if st.button("🌾 Recommend Crop",use_container_width=True):

        data=np.array([[

            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall

        ]])

        prediction=model.predict(data)

        st.markdown(f"""

<div class="result-box">

<h2>✅ Recommended Crop</h2>

<h1 style="font-size:42px;color:#22C55E;">
🌾 {prediction[0].capitalize()}
</h1>

<p style="font-size:18px;color:white;">
Prediction Generated Successfully
</p>

</div>

""",unsafe_allow_html=True)

  