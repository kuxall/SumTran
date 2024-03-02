import streamlit as st
from text_to_speech.text_to_speech import text_to_speech_app
from translator.translator import detect_language, translate
from summarizer.summarizer import summarize_text
from reader import read_txt, read_docx, read_pdf


def handle_translation_error(error):
    """Handles errors during translation and displays informative messages."""
    st.error(f"An error occurred during translation: {error}")


def is_text_empty(text):
    """Checks if the entered text is empty."""
    return not text.strip()


def get_file_contents(uploaded_file):
    """Reads and returns the contents of the uploaded file."""
    if uploaded_file is not None:
        file_contents = uploaded_file.getvalue()

        if uploaded_file.type == "text/plain":
            return read_txt(file_contents)
        elif uploaded_file.type == "application/pdf":
            return read_pdf(file_contents)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return read_docx(file_contents)
        else:
            st.error("Unsupported file format")
    return ""


def translate_text(dummy_text):
    """Translates the text to the selected target language."""
    if not is_text_empty(dummy_text):
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


def main():
    st.sidebar.title("Choose an Option")
    option = st.sidebar.selectbox(
        "Select the Purpose", ["Text-to-Speech", "Translator", "Summarize"]
    )

    if option == "Text-to-Speech":
        text_to_speech_app()

    elif option == "Translator":
        st.title("Language Translator")

        uploaded_file = st.file_uploader(
            "Upload file (TXT, DOCX, PDF)", type=["txt", "docx", "pdf"])
        dummy_text = get_file_contents(uploaded_file)
        st.text_area("File Content", dummy_text)

        if st.button("Translate"):
            translate_text(dummy_text)

    elif option == "Summarize":
        st.title("Text Summarizer")

        uploaded_file = st.file_uploader(
            "Upload file (TXT, DOCX, PDF)", type=["txt", "docx", "pdf"])
        text_to_summarize = get_file_contents(uploaded_file)
        st.text_area("File Content", text_to_summarize)

        if st.button("Summarize"):
            if not is_text_empty(text_to_summarize):
                try:
                    summary_text = summarize_text(text_to_summarize)
                    st.subheader("Summary:")
                    st.write(summary_text)
                except Exception as e:
                    st.error(f"An error occurred during summarization: {e}")
            else:
                st.warning("Please enter some text to summarize.")


if __name__ == "__main__":
    main()
