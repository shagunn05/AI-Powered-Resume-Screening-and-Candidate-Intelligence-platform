import re


def extract_information(text: str):
    """
    Extract candidate basic information from resume.
    """

    # -------------------------
    # Email
    # -------------------------
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    email = re.search(email_pattern, text)

    email = email.group() if email else None

    # -------------------------
    # Phone Number
    # -------------------------
    phone_pattern = r"(\+91[-\s]?)?[6-9]\d{9}"

    phone = re.search(phone_pattern, text)

    phone = phone.group() if phone else None

    # -------------------------
    # Name
    # (Simple Approach)
    # -------------------------

    lines = text.split("\n")

    name = "not found"

    for line in lines:
        line = line.strip()

        if len(line.split()) >= .2 and len(line.split()) <= 4:
            name = line
            break

    
        else:
             name = "Not Found"

    return {
        "name": name,
        "email": email,
        "phone": phone
    }