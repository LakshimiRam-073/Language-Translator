import streamlit as st
from util import *

st.title("Translation")

text = ""
def convert():
    print(text)
    res = fuc(option1, option2, text)
    return res

col1, col2  = st.columns(2)
with col1:
    option1 = st.selectbox(
        'Select input language',
        ('English', 'Hindi', 'Tamil', 'Marathi'))
    text = st.text_area("Enter text here...", height=200)
with col2:
    option2 = st.selectbox(
        'Select output language',
        ('English', 'Hindi','Tamil'))
    st.text_area(label="Translation", value=convert(), height=200)

st.button("Translate")







# text ="தரவு என்பது பொறிமுறையின் கட்டுப்பாட்டு ஓட்டமாகும்"


