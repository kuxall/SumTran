import streamlit as st
from gtts import gTTS

st.title("Text-to-Speech App")

text_to_speak = st.text_input("Enter text to convert to speech:")

language = st.selectbox("Select language:", ["en", "ne", "fr", "es", "de"])

if st.button("Convert to Speech"):
    try:
        # Create a gTTS object
        tts = gTTS(text=text_to_speak, lang=language)

        tts.save("output.mp3")

        st.success("Audio file generated successfully!")
        st.audio("output.mp3")
    except Exception as e:
        st.error(f"Error: {e}")
