import streamlit as st
from gtts import gTTS
from translator import translate
from summarizer import summarize_text


def main():
    st.sidebar.title("Choose an Option")
    option = st.sidebar.selectbox(
        "Select the Purpose", ["Text-to-Speech", "Translator", "Summarize"])

    if option == "Text-to-Speech":
        st.title("Text-to-Speech App")
        text_to_speak = st.text_input("Enter text to convert to speech:")
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
