"""
PDF Service
Handles:
1. PDF Validation
2. PDF Text Extraction
3. DOCX Text Extraction
"""

import os
import pdfplumber
from PyPDF2 import PdfReader
from docx import Document


class PDFService:

    ALLOWED_EXTENSIONS = {"pdf", "docx"}

    @staticmethod
    def allowed_file(filename):

        return "." in filename and \
               filename.rsplit(".", 1)[1].lower() in PDFService.ALLOWED_EXTENSIONS

    @staticmethod
    def extract_pdf_text(file_path):

        text = ""

        try:
            with pdfplumber.open(file_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

        except Exception:

            reader = PdfReader(file_path)

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text.strip()

    @staticmethod
    def extract_docx_text(file_path):

        document = Document(file_path)

        text = []

        for paragraph in document.paragraphs:
            text.append(paragraph.text)

        return "\n".join(text)

    @staticmethod
    def extract_text(file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return PDFService.extract_pdf_text(file_path)

        if extension == ".docx":
            return PDFService.extract_docx_text(file_path)

        raise ValueError("Unsupported file format.")