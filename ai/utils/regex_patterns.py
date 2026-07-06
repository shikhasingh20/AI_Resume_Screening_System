import re

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

PHONE_REGEX = r"(\+91[- ]?)?[6-9]\d{9}"

LINKEDIN_REGEX = r"https?://(www\.)?linkedin\.com/in/\S+"

GITHUB_REGEX = r"https?://(www\.)?github\.com/\S+"

URL_REGEX = r"https?://\S+"

PINCODE_REGEX = r"\b\d{6}\b"

YEAR_REGEX = r"\b(19|20)\d{2}\b"

CGPA_REGEX = r"\b\d\.\d{1,2}\b"

PERCENTAGE_REGEX = r"\b\d{1,3}%\b"