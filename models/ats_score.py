"""
ATS Score Engine
"""


class ATSScore:

    @staticmethod
    def calculate(

        similarity,

        matched_skills,

        total_required_skills,

        education_score,

        experience_score

    ):

        if total_required_skills == 0:

            skill_percent = 0

        else:

            skill_percent = (

                matched_skills /

                total_required_skills

            ) * 100

        ats = (

            similarity * 0.40 +

            skill_percent * 0.30 +

            education_score * 0.20 +

            experience_score * 0.10

        )

        return round(ats, 2)