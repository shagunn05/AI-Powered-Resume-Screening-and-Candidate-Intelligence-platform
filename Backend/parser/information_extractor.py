import re


def extract_information(text: str):
    print("TEXT RECEIVED:")
    print(text)

    print("\nLINES:")
    for i, line in enumerate(text.splitlines(), start=1):
     print(i, repr(line))
     
    # -------------------------
    # Email
    # -------------------------
    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    email = email_match.group(0) if email_match else None

    # -------------------------
    # Phone
    # -------------------------
    phone_match = re.search(
        r"(\+91[\-\s]?)?[6-9]\d{9}",
        text
    )

    phone = phone_match.group(0) if phone_match else None

    # -------------------------
    # Name
    # -------------------------
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    name = "Not Found"

    ignore = [
        "resume",
        "summary",
        "experience",
        "education",
        "skills",
        "projects",
        "certifications",
        "technical skills",
        "contact",
        "email",
        "phone",
        "linkedin",
        "github"
    ]

    for line in lines:

        lower = line.lower()

        if any(word in lower for word in ignore):
            continue

        if "@" in line:
            break

        if re.search(r"\d", line):
            continue

        words = line.split()

        if 2 <= len(words) <= 4:
            name = line
            break

    return {
        "name": name,
        "email": email,
        "phone": phone
    }