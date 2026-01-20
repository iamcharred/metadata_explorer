import streamlit as st
import constants


from services.storage_service import StorageService
import ui_constants
from utils import add_logo


my_logo = add_logo(logo_path="media/logo.jpeg", width=240, height=240)

logo_row = st.columns(3)
logo_row[1].image(my_logo)
# st.image(my_logo)

if ui_constants.SERVICE_STORAGE not in st.session_state:
    with st.spinner('Getting your experience ready...'):
        # Services initialization
        st.session_state[ui_constants.SERVICE_STORAGE] = StorageService([constants.INPUT_BUCKET, constants.OUTPUT_BUCKET], constants.SERVICE_ACCOUNT_KEY_FILE)

header_row = st.columns([6,1], vertical_alignment="center")
header_row[0].title("Metadata explorer")

# Page definition
st.write("Editorial Solaris, leverages LLM multimodal capabilities to revolutionize digital content management. By seamlessly combining information from audio and video, AI generates rich metadata that allows users to effortlessly search, organize, and explore their digital libraries with unprecedented ease and efficiency.  This means you can use the metadata to quickly and easily find the files you're looking for, even if you have a huge collection of audio and video content.")

