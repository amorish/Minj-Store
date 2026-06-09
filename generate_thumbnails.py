import fitz
import os

pdfs = [
    r"past work\2024 st george\output\ST GEORGE HIGH SCHOOL class 6 math question paper.pdf",
    r"past work\2024 st george\output\ST GEORGE HIGH SCHOOL class 7 math question paper.pdf",
    r"past work\2025 Pragati\pragati poster.pdf",
    r"past work\2025 side project\irpe logo design.pdf"
]

for pdf_path in pdfs:
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # first page
        pix = page.get_pixmap(dpi=150)
        out_path = pdf_path.replace('.pdf', '.png')
        pix.save(out_path)
        print(f"Saved {out_path}")
    except Exception as e:
        print(f"Error on {pdf_path}: {e}")
