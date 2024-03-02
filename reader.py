# reader.py
from io import BytesIO
import docx
import PyPDF2


def read_txt(file):
    """Reads text from a TXT file."""
    return BytesIO(file).read().decode("utf-8")


def read_docx(file):
    """Reads text from a DOCX file."""
    docx_text = ""
    try:
        doc = docx.Document(BytesIO(file))
        for para in doc.paragraphs:
            docx_text += para.text + "\n"
    except Exception as e:
        raise RuntimeError(f"Error reading DOCX file: {e}")
    return docx_text


def read_pdf(file):
    """Reads text from a PDF file."""
    pdf_text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(file))
        for page in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page].extract_text() + "/n"
    except Exception as e:
        raise RuntimeError(f"Error reading PDF file: {e}")
    return pdf_text


if __name__ == "__main__":
    filepath = "C:/Users/acer/Desktop/KushalRajSharma/KushalRajSharmaResume.pdf"
    read_content = read_pdf(filepath)
    print(read_content)
