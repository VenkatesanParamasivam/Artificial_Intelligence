# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:05:58 2021

@author: Venkatesan
"""

# import ML_Iris_data
import Introduction
import spacy_highlight_text
import streamlit as st
from Whatsapp import whatsapp_app as whatsapp_analyser
import text_preprocessing
PAGES = {
    # "Machine Learning - Classification": ML_Iris_data,
    "Introduction":Introduction,
    "NLP - Entity Extraction": spacy_highlight_text,
    "Whatsapp Analyser":whatsapp_analyser,
    "NLP - Text Analytics (Preprocessing)":text_preprocessing
}
st.sidebar.title('Artificial Intelligence')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

