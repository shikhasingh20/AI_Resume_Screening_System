"""
====================================================
AI Resume Scoring Service
====================================================

This service is responsible for coordinating
the complete AI Resume Screening Pipeline.

Author : Shikha Singh
Project: AI Resume Screening System
====================================================
"""

from services.pdf_service import PDFService
from services.jd_service import JDService

from models.resume_parser import ResumeParser
from models.text_preprocessor import TextPreprocessor
from models.skill_extractor import SkillExtractor
from models.similarity import SimilarityEngine
from models.ats_score import ATSScore


class ScoringService:

    def __init__(self):

        self.preprocessor = TextPreprocessor()

        self.parser = ResumeParser()

        self.skill_extractor = SkillExtractor()

    # =========================================================

    # Main Function

    # =========================================================

    def evaluate_resume(

        self,

        resume_path,

        job_description

    ):

        # -----------------------------------------

        # STEP 1

        # Extract Resume Text

        # -----------------------------------------

        resume_text = PDFService.extract_text(

            resume_path

        )

        # -----------------------------------------

        # STEP 2

        # Clean Resume Text

        # -----------------------------------------

        clean_resume = self.preprocessor.clean(

            resume_text

        )

        # -----------------------------------------

        # STEP 3

        # Parse Resume

        # -----------------------------------------

        parsed_resume = self.parser.parse(

            clean_resume

        )

        # -----------------------------------------

        # STEP 4

        # Resume Skills

        # -----------------------------------------

        resume_skills = self.skill_extractor.extract(

            clean_resume

        )

        # -----------------------------------------

        # STEP 5

        # Process Job Description

        # -----------------------------------------

        clean_job = JDService.clean(

            job_description

        )

        job_skills = self.skill_extractor.extract(

            clean_job

        )

        # -----------------------------------------

        # STEP 6

        # Similarity Score

        # -----------------------------------------

        similarity_score = SimilarityEngine.calculate(

            clean_resume,

            clean_job

        )

        # -----------------------------------------

        # STEP 7

        # Matching Skills

        # -----------------------------------------

        matched_skills = list(

            set(resume_skills)

            &

            set(job_skills)

        )

        missing_skills = list(

            set(job_skills)

            -

            set(resume_skills)

        )

        # -----------------------------------------

        # STEP 8

        # Education Score

        # (Temporary)

        # -----------------------------------------

        education_score = 80

        # -----------------------------------------

        # STEP 9

        # Experience Score

        # (Temporary)

        # -----------------------------------------

        experience_score = 70

        # -----------------------------------------

        # STEP 10

        # ATS Score

        # -----------------------------------------

        ats = ATSScore.calculate(

            similarity=similarity_score,

            matched_skills=len(matched_skills),

            total_required_skills=len(job_skills),

            education_score=education_score,

            experience_score=experience_score

        )

        # -----------------------------------------

        # Final Result

        # -----------------------------------------

        result = {

            "resume_text": resume_text,

            "parsed_resume": parsed_resume,

            "resume_skills": resume_skills,

            "job_skills": job_skills,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "similarity_score": similarity_score,

            "education_score": education_score,

            "experience_score": experience_score,

            "ats_score": ats

        }

        return result