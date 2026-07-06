"""
=========================================================
AI Resume Screening System
Text Preprocessor
=========================================================
"""

import re
import string
import contractions
import unidecode
import nltk
import spacy

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# English stopwords
STOP_WORDS = set(stopwords.words("english"))


class TextPreprocessor:

    def __init__(self):
        pass

    def lowercase(self, text):
        return text.lower()

    def remove_urls(self, text):
        return re.sub(r"http\S+|www\S+", "", text)

    def remove_emails(self, text):
        return re.sub(r'\S+@\S+', '', text)

    def remove_phone_numbers(self, text):
        return re.sub(r'(\+91[- ]?)?[6-9]\d{9}', '', text)

    def remove_special_characters(self, text):
        return text.translate(
            str.maketrans('', '', string.punctuation)
        )

    def normalize_unicode(self, text):
        return unidecode.unidecode(text)

    def expand_contractions(self, text):
        return contractions.fix(text)

    def remove_extra_spaces(self, text):
        return re.sub(r"\s+", " ", text).strip()

    def tokenize(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        return [
            word
            for word in tokens
            if word not in STOP_WORDS
        ]

    def lemmatize(self, tokens):

        sentence = " ".join(tokens)

        doc = nlp(sentence)

        return [token.lemma_ for token in doc]

    def preprocess(self, text):

        text = self.normalize_unicode(text)

        text = self.expand_contractions(text)

        text = self.lowercase(text)

        text = self.remove_urls(text)

        text = self.remove_emails(text)

        text = self.remove_phone_numbers(text)

        text = self.remove_special_characters(text)

        text = self.remove_extra_spaces(text)

        tokens = self.tokenize(text)

        tokens = self.remove_stopwords(tokens)

        tokens = self.lemmatize(tokens)

        return " ".join(tokens)