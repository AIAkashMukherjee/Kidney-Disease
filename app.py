import streamlit as st
from PIL import Image
import os
from src.pipeline.prediction_pipeline import PredictionPipeline  # Assuming your PredictionPipeline is saved in this file

# Streamlit interface
st.title('Kidney Tumor Detection')


# File uploader
uploaded_file = st.file_uploader("Choose a CT scan image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded image to a temporary directory
    img_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image.", use_container_width=True)

    # Initialize PredictionPipeline
    pipeline = PredictionPipeline(file_name=img_path)

    # Make the prediction
    st.write("Processing image...")
    prediction = pipeline.predict()

    # Display the result
    prediction_result = prediction[0]["image"]

    
    st.write(f"Prediction: {prediction_result}")

    # Optionally, remove the temporary image after processing
    os.remove(img_path)