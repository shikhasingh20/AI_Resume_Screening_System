import pdfplumber


def extract_resume_text(pdf_path):
    """
    Extract text from PDF resume
    """

    text = ""

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + " "

    except Exception as e:

        print("Error:", e)

    return text