
import streamlit as st
from src.data_loader.load_images import load_images_from_folder
from src.preprocessing.image_preprocessing import preprocess_image
from src.ocr.extract_text import extract_text_from_image
from src.nlp.field_extraction import extract_fields

st.title('VisionOCR - Leitura Automática de Documentos')

uploaded_files = st.file_uploader('Envie imagens de documentos', type=['png','jpg','jpeg'], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        st.image(file, caption='Documento Original')
        img_bin = preprocess_image(file)
        st.image(img_bin, caption='Pré-processado', channels='GRAY')
        text = extract_text_from_image(img_bin)
        st.text_area('Texto Extraído', text, height=200)
        fields = extract_fields(text)
        st.json(fields)
