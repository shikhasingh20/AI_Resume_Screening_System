"""
Text Preprocessor

Responsible for:
- Lowercasing
- Removing punctuation
- Removing numbers
- Removing stopwords
- Lemmatization
"""

import re

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer

from nltk.tokenize import word_tokenize


class TextPreprocessor:

    def __init__(self):

        self.stop_words = set(

            stopwords.words("english")

        )

        self.lemmatizer = WordNetLemmatizer()

    def clean(self, text):

        text = text.lower()

        text = re.sub(

            r"[^a-zA-Z ]",

            " ",

            text

        )

        tokens = word_tokenize(text)

        words = []

        for word in tokens:

            if word not in self.stop_words:

                word = self.lemmatizer.lemmatize(word)

                words.append(word)

        return " ".join(words)