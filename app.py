
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import os
import glob

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Animal Image Classification",
    page_icon="🦁",
    layout="centered"
)

st.title("🦁 Animal Image Classification")
st.write("Upload an image of a Lion, Leopard, or Horse.")

# --------------------------------------------------
# Find Model Automatically
# --------------------------------------------------

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Search for .keras and .h5 model files
keras_files = glob.glob(os.path.join(APP_FOLDER, "*.keras"))
h5_files = glob.glob(os.path.join(APP_FOLDER, "*.h5"))

model_files = keras_files + h5_files

# --------------------------------------------------
# Display Files Found
# --------------------------------------------------

with st.expander("🔍 Check Model Files"):
    st.write("App folder:")
    st.code(APP_FOLDER)

    st.write("Files found in app folder:")

    all_files = os.listdir(APP_FOLDER)

    for file in all_files:
        st.write("📄", file)

# --------------------------------------------------
# Load Model
# --------------------------------------------------

@st.cache_resource
def load_animal_model():

    if len(model_files) == 0:
        return None

    model_path = model_files[0]

    st.write("Loading model:")
    st.code(model_path)

    return load_model(model_path)


model = load_animal_model()

# --------------------------------------------------
# Check Model
# --------------------------------------------------

if model is None:

    st.error("❌ Model file not found!")

    st.warning(
        "Please place your .keras or .h5 model file in the same folder as app.py."
    )

    st.stop()

else:

    st.success("✅ Model loaded successfully!")

# --------------------------------------------------
# Class Names
# --------------------------------------------------

class_names = [
    "Lion",
    "Leopard",
    "Horse"
]

# --------------------------------------------------
# Upload Image
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload an animal image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        width=300
    )

    # Resize image
    image = image.resize((128, 128))

    # Convert to NumPy array
    img_array = np.array(image)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)

    predicted_class = np.argmax(prediction[0])

    confidence = np.max(prediction[0]) * 100

    # --------------------------------------------------
    # Result
    # --------------------------------------------------

    st.subheader("🔎 Prediction")

    st.write(
        f"### Animal: {class_names[predicted_class]}"
    )

    st.write(
        f"### Confidence: {confidence:.2f}%"
    )



