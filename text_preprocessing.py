# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:53:57 2022

@author: Venkatesan
"""

import ftfy
import streamlit as st

def app():
    c1, c2 = st.columns([3, 1])
    
    if c2.button("Try Demo"):
        
        st.warning('Input text:::'+ 'The Mona Lisa doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have eyebrows.')
    
        st.success(ftfy.fix_text('Cleaned text:::'+ 'The Mona Lisa doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have eyebrows.'))
        
    # t=c1.button("text input"):
    input_text=st.text_area("Enter your input here")
    if input_text:
        st.write(ftfy.fix_text(input_text))