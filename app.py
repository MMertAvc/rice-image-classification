import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load your trained model with error handling
try:
    model = load_model('my_rice_cnn_model.h5')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Define a function to preprocess the image
def process_image(img):
    """
    Preprocess the uploaded image for model prediction.
    Resizes to 64x64, normalizes, and adds batch dimension.
    """
    img = img.resize((64, 64))  # Resize to match the input shape of the model
    img = np.array(img)
    img = img / 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Streamlit app title
st.title("Rice Class Classification")
st.write("Upload a Picture")

# Upload the file
file = st.file_uploader("Select an Image", type=['jpg', 'jpeg', 'png'])

if file is not None:
    try:
        img = Image.open(file)
        st.image(img, caption='Uploaded Image', use_column_width=True)
        image = process_image(img)
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)
        
        class_names = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']
        st.write(f"Predicted Class: {class_names[predicted_class]}")
    except Exception as e:
        st.error(f"Error processing image: {e}")