import streamlit as st
from transformers import pipeline


@st.cache_data()
def summarize_text(text):
    summarizer = pipeline("summarization", model="google-t5/t5-small")
    summary = summarizer(text)
    return summary[0]['summary_text']
