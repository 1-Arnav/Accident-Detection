import streamlit as st
from predictor import predict
from imgChooser import load_images, img_option

st.set_page_config(page_title="Accident Detecton", page_icon= ":collision:", layout="centered")
st.title(" Accident Detection using machine learning")
st.divider()


uploaded_file = st.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg'])

try:
    st.write(predict(uploaded_file))
except:
    st.warning("Please upload a file")

if uploaded_file is not None:
    st.image(uploaded_file)

st.markdown('#')
st.subheader("OR Choose from below")
st.markdown('#')

col1, col2 = st.columns(2)
col2.markdown("###")

with col1:
    img_files, manuscripts = load_images()
    view_manuscripts = st.multiselect("Select Folder(s)", manuscripts, key=1)
    try:
        im =img_option(img_files, view_manuscripts)
    except:
        col2.warning("Please choose a folder")
    # st.write(im)

with col2:
    with st.container(border=True):
        try:
            st.write(predict(im))
            st.image(im)
        except:
            pass
