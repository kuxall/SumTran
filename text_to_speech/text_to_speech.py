# text_to_speech/text_to_speech.py
import streamlit as st
from gtts import gTTS


def text_to_speech_app():
    st.title("Text-to-Speech App")

    uploaded_file = st.file_uploader("Choose a text file", type="txt")
    if uploaded_file is not None:
        text_to_speak = uploaded_file.read().decode()

        language = st.selectbox("Select language:", [
                                "en", "ne", "fr", "es", "de"])

        if st.button("Convert to Speech"):
            try:
                tts = gTTS(text=text_to_speak, lang=language)
                tts.save("output.mp3")
                st.success("Audio file generated successfully!")
                st.audio("output.mp3")
            except Exception as e:
                st.error(f"Error: {e}")
