import requests
import streamlit as st
from langdetect import detect

# Language detection function
def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "unknown"

# Translation function
def translate(src, trg, text):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src}&tl={trg}&dt=t&dt=bd&dj=1&q={text}"
    response = requests.get(url)
    if response.ok:
        result = response.json()
        translated_text = ""
        for sentence_data in result["sentences"]:
            translated_text += sentence_data["trans"]
        return translated_text
    else:
        st.error("Translation request failed.")
        return None
