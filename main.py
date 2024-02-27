# main.py
import streamlit as st
from text_to_speech.text_to_speech import text_to_speech_app
from translator.translator import translate
from summarizer.summarizer import summarize_text


def main():
    st.sidebar.title("Choose an Option")
    option = st.sidebar.selectbox(
        "Select the Purpose", ["Text-to-Speech", "Translator", "Summarize"])

    if option == "Text-to-Speech":
        text_to_speech_app()

    elif option == "Translator":
        st.title("Language Translator")
        dummy_text = st.text_area("Enter the text you want to translate")
        target_language = st.selectbox("Select Target Language", [
            "Nepali", "French", "Spanish", "German", "Chinese", "Japanese", "Korean", "Russian", "Italian", "Arabic",
            "Portuguese", "Dutch", "Swedish", "Danish", "Finnish", "Greek", "Hebrew", "Hindi", "Turkish"
        ])

        if st.button("Translate"):
            if dummy_text:
                language_codes = {
                    "Nepali": "ne", "French": "fr", "Spanish": "es", "German": "de", "Chinese": "zh-CN",
                    "Japanese": "ja", "Korean": "ko", "Russian": "ru", "Italian": "it", "Arabic": "ar",
                    "Portuguese": "pt", "Dutch": "nl", "Swedish": "sv", "Danish": "da", "Finnish": "fi",
                    "Greek": "el", "Hebrew": "iw", "Hindi": "hi", "Turkish": "tr"
                }
                trg_lang_code = language_codes.get(target_language)

                translated_text = translate(
                    src="en", trg=trg_lang_code, text=dummy_text)
                if translated_text:
                    st.success("Translated Text:")
                    st.write(translated_text)
            else:
                st.warning("Please enter some text for translation.")

    elif option == "Summarize":
        st.title("Text Summarizer")
        text = st.text_area("Please input the text to summarize")
        if st.button("Summarize"):
            if text:
                summary_text = summarize_text(text)
                st.subheader("Summary:")
                st.write(summary_text)
            else:
                st.warning("Please enter some text to summarize.")


if __name__ == "__main__":
    main()
