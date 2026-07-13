import re


def clean_jd(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()