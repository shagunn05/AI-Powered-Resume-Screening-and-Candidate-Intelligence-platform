import re


def clean_text(text: str) -> str:
    """
    Clean extracted resume text.
    """

    # Remove extra spaces and newlines
    text = re.sub(r"\s+", " ", text)

    # Remove null characters
    text = text.replace("\x00", "")

    # Remove leading/trailing spaces
    text = text.strip()

    return text