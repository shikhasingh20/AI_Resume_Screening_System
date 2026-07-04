"""
==============================================
Industry Level Resume Parser
==============================================
"""

import re
import spacy

nlp = spacy.load("en_core_web_sm")


class ResumeParser:

    def parse(self, text):

        doc = nlp(text)

        data = {

            "name": self.extract_name(doc),

            "email": self.extract_email(text),

            "phone": self.extract_phone(text),

            "linkedin": self.extract_linkedin(text),

            "github": self.extract_github(text),

            "education": self.extract_education(text),

            "experience": self.extract_experience(text),

            "projects": self.extract_projects(text),

            "certifications": self.extract_certifications(text)

        }

        return data

    # ----------------------------------

    def extract_name(self, doc):

        for ent in doc.ents:

            if ent.label_ == "PERSON":

                return ent.text

        return ""

    # ----------------------------------

    def extract_email(self, text):

        match = re.search(

            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

            text

        )

        return match.group() if match else ""

    # ----------------------------------

    def extract_phone(self, text):

        match = re.search(

            r'(\+91[- ]?)?[6-9]\d{9}',

            text

        )

        return match.group() if match else ""

    # ----------------------------------

    def extract_linkedin(self, text):

        match = re.search(

            r'https?://(www\.)?linkedin\.com/in/\S+',

            text

        )

        return match.group() if match else ""

    # ----------------------------------

    def extract_github(self, text):

        match = re.search(

            r'https?://(www\.)?github\.com/\S+',

            text

        )

        return match.group() if match else ""

    # ----------------------------------

    def extract_education(self, text):

        degrees = [

            "BCA",

            "MCA",

            "B.Tech",

            "M.Tech",

            "B.Sc",

            "M.Sc",

            "MBA",

            "BE",

            "ME"

        ]

        found = []

        for degree in degrees:

            if degree.lower() in text.lower():

                found.append(degree)

        return found

    # ----------------------------------

    def extract_experience(self, text):

        match = re.search(

            r'(\d+)\+?\s*(year|years)',

            text.lower()

        )

        if match:

            return int(match.group(1))

        return 0

    # ----------------------------------

    def extract_projects(self, text):

        lines = text.split("\n")

        projects = []

        capture = False

        for line in lines:

            if "project" in line.lower():

                capture = True

                continue

            if capture:

                if line.strip() == "":

                    break

                projects.append(line.strip())

        return projects

    # ----------------------------------

    def extract_certifications(self, text):

        certs = [

            "AWS",

            "Azure",

            "Oracle",

            "Google",

            "Microsoft",

            "Coursera",

            "Udemy"

        ]

        found = []

        for cert in certs:

            if cert.lower() in text.lower():

                found.append(cert)

        return found
    