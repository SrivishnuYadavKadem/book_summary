import PyPDF2
import re
from models.general_formatter import GeneralFormatter
from models.general_formatter import GeneralFormatter

class PDFProcessor:
    def extract_text(self, pdf_path):
        """
        Extract text from a PDF file
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
        """
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        
        # Fix common PDF extraction issues
        text = self._fix_word_splitting(text)
        
        # Apply general formatter to fix spacing issues
        text = GeneralFormatter.format_text(text)
        
        return text
    
    def _fix_word_splitting(self, text):
        """
        Fix common PDF extraction issues like incorrectly split words
        
        Args:
            text (str): Raw extracted text
            
        Returns:
            str: Cleaned text with fixed word splitting
        """
        # First, fix specific technical phrases
        text = re.sub(r'topology\s*\(\s*as\s*shown\s*in\s*F\s*igure', 'topology (as shown in Figure', text)
        text = re.sub(r'data\s*and\s*decision', 'data and decision', text)
        text = re.sub(r'In\s*decentralized\s*systems', 'In decentralized systems', text)
        text = re.sub(r'The\s*topology', 'The topology', text)
        text = re.sub(r'It\s*may\s*be\s*any\s*existing\s*application', 'It may be any existing application', text)
        text = re.sub(r'Clients\s*are\s*restricted\s*using', 'Clients are restricted using', text)
        text = re.sub(r'Public\s+Key\s+Infrastructure\s*\(\s*PKI\s*\)', 'Public Key Infrastructure (PKI)', text)
        text = re.sub(r'technology\s*at\s*blockchain', 'technology at blockchain', text)
        
        # Fix words with no spaces between them
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Split camelCase
        text = re.sub(r'Indecentralizedsystems', r'In decentralized systems', text)
        text = re.sub(r'dataanddecision', r'data and decision', text)
        text = re.sub(r'thedataanddecisions', r'the data and decisions', text)
        text = re.sub(r'Itmaybeanyexistingapplication', r'It may be any existing application', text)
        text = re.sub(r'Clientsarerestrictedusing', r'Clients are restricted using', text)
        
        # Fix words split with spaces in the middle
        text = re.sub(r'([a-z])\s+([a-z])', r'\1\2', text)
        
        # Fix words split with spaces after/before common prefixes/suffixes
        prefixes = ['de', 'in', 're', 'pre', 'pro', 'con', 'com', 'ex', 'en', 'em', 'un']
        for prefix in prefixes:
            text = re.sub(fr'{prefix}\s+([a-z])', fr'{prefix}\1', text)
        
        # Fix common patterns like "p ersonalized" -> "personalized"
        text = re.sub(r'([a-z])\s+([aeiouy][a-z])', r'\1\2', text)
        
        # Fix incorrectly split words with hyphens
        text = re.sub(r'([a-z])-\s*([a-z])', r'\1\2', text)
        
        # Fix technical document patterns
        text = re.sub(r'F\s+igure', r'Figure', text)
        text = re.sub(r'as\s+shown\s+in', r'as shown in', text)
        text = re.sub(r'Public\s+Key\s+Infrastructure', r'Public Key Infrastructure', text)
        text = re.sub(r'blockchain\s+technology', r'blockchain technology', text)
        text = re.sub(r'data\s+and\s+decision', r'data and decision', text)
        text = re.sub(r'decentralized\s+systems', r'decentralized systems', text)
        text = re.sub(r'PKI\s+technology', r'PKI technology', text)
        
        # Fix common resume patterns
        text = re.sub(r'([A-Za-z])\s+(\d{3})\s*-\s*(\d{3})\s*-\s*(\d{4})', r'\1 \2-\3-\4', text)  # Phone numbers
        text = re.sub(r'([A-Za-z])\s+(\d{5,6})', r'\1 \2', text)  # ZIP codes
        
        # Fix education formatting
        text = re.sub(r'B\.\s*T\s*ech', r'B.Tech', text)  # Fix B.Tech
        text = re.sub(r'C\s*G\s*P\s*A\s*:', r'CGPA:', text)  # Fix CGPA
        text = re.sub(r'(\d{4})\s*-\s*(\d{4})', r'\1-\2', text)  # Fix year ranges
        
        # Fix percentage formatting
        text = re.sub(r'P\s*ercentage\s*:', r'Percentage:', text)
        text = re.sub(r'(\d+(?:\.\d+)?)\s*%', r'\1%', text)  # Fix percentages
        
        # Fix school and college names
        text = re.sub(r'([a-z])college([a-z])', r'\1 College \2', text)
        text = re.sub(r'junior\s*college', r'Junior College', text)
        text = re.sub(r'([A-Za-z])\s+School', r'\1 School', text)  # Fix school names
        text = re.sub(r'Little\s+Flower', r'Little Flower', text)  # Fix specific school name
        
        # Fix skills section
        text = re.sub(r'Skills\s+Programming', r'Skills\nProgramming', text)
        text = re.sub(r'Languages\s*:', r'Languages:', text)
        
        # Add spaces between sentences and sections
        text = re.sub(r'\.([A-Z])', r'. \1', text)
        text = re.sub(r'(\d+)\.(\d+)', r'\1.\2', text)  # Preserve decimal points
        
        # Final cleanup of any remaining issues
        text = re.sub(r'\s+-\s*\.', r'.', text)  # Remove dangling hyphens
        text = re.sub(r'\s+\.', r'.', text)  # Fix spaces before periods
        text = re.sub(r'\s{2,}', r' ', text)  # Remove multiple spaces
        
        return text