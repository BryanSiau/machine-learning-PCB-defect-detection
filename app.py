import streamlit as st
from PIL import Image
import cv2
import detect as detect
import argparse

st.set_page_config(page_title="My webpage")

#SIDEBAR SECTION
st.sidebar.title("Settings")
#st.sidebar.markdown("---")
#st.markdown
st.sidebar.write("This is a sidebar")

confidence = st.sidebar.slider("Set Confidence Level: ", min_value= 0.0, max_value= 1.0, value=0.70, step=0.01)
st.sidebar.write("Confidence: ", confidence)
st.sidebar.markdown("---")

#Sidebar - File Upload
st.sidebar.title("Upload Image")


#HEADER SECTION 
st.title("PCB Defect Detection")
st.write("This is a demo of a PCB defect detection model")


#Upload Image
@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img

uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
if uploaded_file is not None:
    picture = Image.open(uploaded_file)
    picture = picture.save(f'data/images/{uploaded_file.name}')
    st.sidebar.text("Original Image")
    st.sidebar.image(uploaded_file)
    

#detection
if st.sidebar.button("Detect"):
    #detect(uploaded_file, confidence)
    #python detect.py --source ./data/images/888.jpg --weights ./weights/best.pt
    detect.run(source = picture)
    st.sidebar.write("Detecting...")
    st.sidebar.write("Done!")



st.sidebar.markdown("---")
st.sidebar.write("Live Detection")
run = st.sidebar.checkbox('Run Camera')
# FRAME_WINDOW = st.image([])
# camera = cv2.VideoCapture(0)

while run:
    # _, frame = camera.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # FRAME_WINDOW.image(frame)
    detect.run(source= 0 )