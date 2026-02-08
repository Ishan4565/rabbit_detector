import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# This is the exact, unchangeable path to your model
model_path = r'C:\Users\dell\Desktop\data\models\rabbit_detector.h5'

if not os.path.exists(model_path):
    st.error(f"❌ STOP: The file is NOT at {model_path}")
    st.info("Check your 'data' folder. Do you see 'models' inside it? Is 'rabbit_detector.h5' inside that?")
    st.stop()

@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model(model_path)

try:
    model = load_my_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("🐰 Rabbit Detector")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    img = image.resize((160, 160))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = (img_array / 127.5) - 1

    prediction = model.predict(img_array)
    score = float(prediction[0][0]) 

    if score > 0.5:
        st.success(f"It's a RABBIT! ({score:.2%})")
    else:
        st.info(f"Not a rabbit. ({1-score:.2%})")