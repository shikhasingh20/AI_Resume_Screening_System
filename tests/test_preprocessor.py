import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.preprocessing.text_preprocessor import TextPreprocessor

processor = TextPreprocessor()

sample_text = """
John Doe

Email: john@gmail.com

Phone: +91 9876543210

Skills:
Python Java SQL Machine Learning

GitHub:
https://github.com/johndoe
"""

print("Original Text:")
print(sample_text)

print("\nProcessed Text:")
print(processor.preprocess(sample_text))