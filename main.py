from pathlib import Path
import streamlit as st
import detect as detect
import os
from PIL import Image


# Returns all sub-directories in a specific Path
def get_subdirs(b='.'):
    result = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd):
            result.append(bd)
    return result

#Returns the latest folder in a runs\detect
def get_detection_folder():
    return max(get_subdirs(os.path.join('runs', 'detect')), key=os.path.getmtime)


if __name__ == '__main__':

    st.set_page_config(page_title="My webpage")

    #HEADER SECTION 
    st.title("PCB Defect Detection")
    st.write("This is a demo for PCB defect detection model")

    #SIDEBAR SECTION
    st.sidebar.title("Settings")
    st.sidebar.markdown("---")

    #Sidebar - File Upload
    st.sidebar.title("Upload Image")
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
    if uploaded_file is not None:
        picture = Image.open(uploaded_file)
        #picture = picture.save(f'data/images/{uploaded_file.name}')
        st.sidebar.text("Original Image")
        st.sidebar.image(uploaded_file)

    #detection
    if st.sidebar.button("Detect"):
        detect.run(source= (f'data/images/{uploaded_file.name}'))

        for img in os.listdir(get_detection_folder()):
                            st.image(str(Path(f'{get_detection_folder()}') / img))


    #Live camera detection
    st.sidebar.markdown("---")
    st.sidebar.write("Start Live Detection")
    run = st.sidebar.checkbox('Run Camera')

    while run:
        detect.run(source= 0)


