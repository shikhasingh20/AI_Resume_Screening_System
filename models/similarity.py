"""
Similarity Engine
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:

    @staticmethod
    def calculate(resume_text, job_text):

        corpus = [

            resume_text,

            job_text

        ]

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform(corpus)

        similarity = cosine_similarity(

            vectors[0:1],

            vectors[1:2]

        )[0][0]

        return round(similarity * 100, 2)