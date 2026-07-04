"""
Extract technical skills from resume text.
"""

import re


class SkillExtractor:

    def __init__(self):

        self.skills = {

            "Programming": [
                "python", "java", "c", "c++", "c#", "javascript",
                "typescript", "php", "go", "rust"
            ],

            "Web": [
                "html", "css", "bootstrap",
                "flask", "django", "react",
                "angular", "vue", "nodejs",
                "express"
            ],

            "Database": [
                "mysql",
                "postgresql",
                "mongodb",
                "oracle",
                "sqlite"
            ],

            "Cloud": [
                "aws",
                "azure",
                "gcp",
                "docker",
                "kubernetes"
            ],

            "AI": [
                "machine learning",
                "deep learning",
                "tensorflow",
                "keras",
                "pytorch",
                "nlp",
                "opencv",
                "pandas",
                "numpy",
                "scikit-learn"
            ],

            "Tools": [
                "git",
                "github",
                "jira",
                "linux",
                "postman"
            ]
        }

    def extract(self, text):

        found = []

        text = text.lower()

        for category in self.skills.values():

            for skill in category:

                pattern = r"\b" + re.escape(skill) + r"\b"

                if re.search(pattern, text):

                    found.append(skill)

        return sorted(list(set(found)))