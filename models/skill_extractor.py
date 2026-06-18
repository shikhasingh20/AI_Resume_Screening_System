SKILLS_DB = [

    "python",
    "java",
    "c++",
    "mysql",
    "postgresql",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "flask",
    "django",
    "git",
    "github",
    "machine learning",
    "deep learning",
    "data analysis",
    "excel"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:

        if skill in text:

            found_skills.append(skill)

    return list(set(found_skills))