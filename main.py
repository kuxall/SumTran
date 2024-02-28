import streamlit as st
from text_to_speech.text_to_speech import text_to_speech_app
from translator.translator import detect_language, translate
from summarizer.summarizer import summarize_text


def handle_translation_error(error):
    """Handles errors during translation and displays informative messages."""
    st.error(f"An error occurred during translation: {error}")


def handle_text_to_speech_error(error):
    """Handles errors during text-to-speech conversion and displays informative messages."""
    st.error(f"An error occurred while converting text to speech: {error}")


def is_text_empty(text):
    """Checks if the entered text is empty."""
    return not text.strip()


def main():
    st.sidebar.title("Choose an Option")
    option = st.sidebar.selectbox(
        "Select the Purpose", ["Text-to-Speech", "Translator", "Summarize"]
    )

    if option == "Text-to-Speech":
        text_to_speech_app()

    elif option == "Translator":
        st.title("Language Translator")

        dummy_text = st.text_area("Enter the text you want to translate:", "")

        if st.button("Detect Language"):
            if dummy_text:
                try:
                    src_language = detect_language(dummy_text)
                    if src_language != "unknown":
                        st.success(f"Detected language: {src_language}")
                    else:
                        st.error("Language detection failed.")
                except Exception as e:
                    handle_translation_error(e)

        target_language = st.selectbox("Select the target language:", [
            "English", "Spanish", "French", "German", "Chinese (Simplified)", "Japanese", "Korean", "Russian", "Italian",
            "Arabic", "Portuguese", "Dutch", "Swedish", "Danish", "Finnish", "Greek", "Hebrew", "Hindi", "Turkish", "Nepali"
        ])

        language_codes = {
            "English": "en", "Spanish": "es", "French": "fr", "German": "de", "Chinese (Simplified)": "zh-CN",
            "Japanese": "ja", "Korean": "ko", "Russian": "ru", "Italian": "it", "Arabic": "ar",
            "Portuguese": "pt", "Dutch": "nl", "Swedish": "sv", "Danish": "da", "Finnish": "fi",
            "Greek": "el", "Hebrew": "iw", "Hindi": "hi", "Turkish": "tr", "Nepali": "ne"
        }

        if st.button("Translate"):
            if not is_text_empty(dummy_text):
                trg_lang_code = language_codes.get(target_language)
                try:
                    src_language = detect_language(dummy_text)
                    if src_language != "unknown":
                        translated_text = translate(
                            src_language, trg_lang_code, dummy_text)
                        if translated_text:
                            st.success("Translation successful:")
                            st.write(translated_text)
                        else:
                            st.error("Translation failed.")
                    else:
                        st.error("Language detection failed.")
                except Exception as e:
                    handle_translation_error(e)
            else:
                st.warning("Please enter text to translate.")

    elif option == "Summarize":
        st.title("Text Summarizer")
        text = st.text_area("Please input the text to summarize")

        if st.button("Summarize"):
            if not is_text_empty(text):
                try:
                    summary_text = summarize_text(text)
                    st.subheader("Summary:")
                    st.write(summary_text)
                except Exception as e:
                    st.error(f"An error occurred during summarization: {e}")
            else:
                st.warning("Please enter some text to summarize.")


if __name__ == "__main__":
    main()
