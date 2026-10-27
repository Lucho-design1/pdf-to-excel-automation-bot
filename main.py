import pdfplumber
import pandas as pd

def extract_invoice(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        # Lógica de procesamiento de datos
        return text

print('Bot de automatización listo. Contactar para implementación personalizada.')