import joblib
import pandas as pd
import os


# ==========================================
# Load Fertilizer Model
# ==========================================

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "fertilizer_model.pkl"
)

fertilizer_model = joblib.load(MODEL_PATH)


# ==========================================
# Fertilizer Name Mapping
# ==========================================

FERTILIZER_NAMES = {
    "Urea": "Urea",

    "DAP": "Diammonium Phosphate (DAP)",

    "14-35-14": "NPK Fertilizer (14-35-14)",

    "28-28": "NPK Fertilizer (28-28-0)",

    "17-17-17": "NPK Fertilizer (17-17-17)",

    "20-20": "NPK Fertilizer (20-20-0)",

    "10-26-26": "NPK Fertilizer (10-26-26)"
}


# ==========================================
# Predict Fertilizer
# ==========================================

def predict_fertilizer(
    temperature,
    humidity,
    moisture,
    soil_type,
    crop_type,
    nitrogen,
    potassium,
    phosphorous
):
    """
    Predict fertilizer based on soil,
    crop and environmental conditions.
    """

    data = pd.DataFrame([{
        "Temperature": temperature,
        "Humidity": humidity,
        "Moisture": moisture,
        "Soil Type": soil_type,
        "Crop Type": crop_type,
        "Nitrogen": nitrogen,
        "Potassium": potassium,
        "Phosphorous": phosphorous
    }])

    # Predict using ML model
    prediction = fertilizer_model.predict(data)

    # Get original prediction
    fertilizer = prediction[0]

    # Convert model label into readable fertilizer name
    fertilizer_name = FERTILIZER_NAMES.get(
        fertilizer,
        fertilizer
    )

    return fertilizer_name