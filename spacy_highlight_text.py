# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 15:23:29 2022

@author: Venkatesan
"""
import streamlit as st
import spacy_streamlit

def app():

    models = ["en_core_web_sm", "en_core_web_md"]
    default_text = "Sundar Pichai is the CEO of Google."
    spacy_streamlit.visualize(models, default_text)