"""
pdf_service.py

Purpose:
--------
Handles all PDF-related operations.

Responsibilities:
1. Validate uploaded PDF.
2. Extract text from PDF.
3. Return clean text.
"""

import os
import pdfplumber


class PDFService:

    ALLOWED_EXTENSIONS = {"pdf"}

    @staticmethod
    def allowed_file(filename: str) -> bool:
        """
        Check if uploaded file is a PDF.
        """

        if "." not in filename:
            return False

        extension = filename.rsplit(".", 1)[1].lower()

        return extension in PDFService.ALLOWED_EXTENSIONS

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """
        Read a PDF and return all text.
        """

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(
                f"File not found: {pdf_path}"
            )

        extracted_text = ""

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + "\n"

        return extracted_text.strip()

    @staticmethod
    def total_pages(pdf_path: str) -> int:
        """
        Return total pages in PDF.
        """

        with pdfplumber.open(pdf_path) as pdf:

            return len(pdf.pages)