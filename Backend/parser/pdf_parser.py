import fitz  # PyMuPDF


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract complete text from a PDF file.
    """

    text = ""

    try:
        pdf_document = fitz.open(file_path)

        for page in pdf_document:
            text += page.get_text()

        pdf_document.close()

        return text.strip()

    except Exception as e:
        raise Exception(f"Error while reading PDF: {e}")