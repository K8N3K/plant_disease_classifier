
import os
import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
 
# ---------------- CONFIG ----------------
MODEL_PATH = "plant_disease_prediction_model.h5"   # change to your actual .h5 filename
IMG_SIZE = (224, 224)
DRIVE_FILE_ID = "/d/1lFrLajWFVjkzBGkei3Q8pZIA-k_XJD-L/view"  # optional: paste Google Drive file ID to auto-download the model
 
CLASS_NAMES = {
    0: 'Pepper__bell___Bacterial_spot',
    1: 'Pepper__bell___healthy',
    2: 'Potato___Early_blight',
    3: 'Potato___Late_blight',
    4: 'Potato___healthy',
    5: 'Tomato_Bacterial_spot',
    6: 'Tomato_Early_blight',
    7: 'Tomato_Late_blight',
    8: 'Tomato_Leaf_Mold',
    9: 'Tomato_Septoria_leaf_spot',
    10: 'Tomato_Spider_mites_Two_spotted_spider_mite',
    11: 'Tomato__Target_Spot',
    12: 'Tomato__Tomato_YellowLeaf__Curl_Virus',
    13: 'Tomato__Tomato_mosaic_virus',
    14: 'Tomato_healthy',
}
# ----------------------------------------
 
 
def pretty(name: str) -> str:
    """Turn 'Tomato_Early_blight' into 'Tomato - Early blight'."""
    name = name.replace("___", " - ").replace("__", " - ")
    parts = name.split("_", 1) if " - " not in name else [name]
    name = " - ".join(parts) if len(parts) == 2 else name
    return name.replace("_", " ")
 
 
@st.cache_resource
def get_model():
    if not os.path.exists(MODEL_PATH) and DRIVE_FILE_ID:
        import gdown
        gdown.download(f"https://drive.google.com/uc?id={DRIVE_FILE_ID}", MODEL_PATH, quiet=False)
    return load_model(MODEL_PATH)
 
 
st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿")
st.title("🌿 Plant Disease Detector")
st.write("Upload a clear photo of a leaf (pepper, potato or tomato) and the model will predict its condition.")
 
model = get_model()
 
uploaded = st.file_uploader("Choose a leaf image", type=["jpg", "jpeg", "png"])
 
if uploaded is not None:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded image", use_container_width=True)
 
    arr = np.array(img.resize(IMG_SIZE), dtype="float32")
    arr = np.expand_dims(arr, axis=0) / 255.0  # remove /255.0 if your model was trained without rescaling
 
    with st.spinner("Analyzing..."):
        preds = model.predict(arr)[0]
 
    top = int(np.argmax(preds))
    st.success(f"**Prediction:** {pretty(CLASS_NAMES[top])}")
    st.info(f"**Confidence:** {preds[top] * 100:.2f}%")
 
    st.subheader("Top 3 predictions")
    for i in np.argsort(preds)[-3:][::-1]:
        st.write(f"- {pretty(CLASS_NAMES[int(i)])}: {preds[i] * 100:.2f}%")