import PyPDF2
from models.text_utils import TextUtils

class PDFUtils:
    """Simplified PDF utilities for extracting and processing PDF content"""
    
    @staticmethod
    def extract_text(pdf_path):
        """Extract text from a PDF file and fix common formatting issues"""
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        
        # Fix spacing issues
        text = TextUtils.fix_spacing(text)
        
        return text