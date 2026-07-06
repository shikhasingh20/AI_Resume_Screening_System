from services.pdf_service import PDFService

resume = "uploads/resumes/sample_resume.pdf"

text = PDFService.extract_text(resume)

print("=" * 50)
print(text)
print("=" * 50)