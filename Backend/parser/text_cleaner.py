import re

def clean_text(text: str) -> str:
    """
    Clean extracted resume text while preserving line breaks.
    """

    # Remove null characters
    text = text.replace("\x00", "")

    # Remove extra spaces but preserve new lines
    lines = []

    for line in text.splitlines():

        line = re.sub(r"\s+", " ", line).strip()

        if line:
            lines.append(line)

    return "\n".join(lines)