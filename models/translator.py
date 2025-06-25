import requests

class SimpleTranslator:
    """A simple translator using LibreTranslate API"""
    
    def __init__(self):
        # LibreTranslate API endpoint (public instance)
        self.api_url = "https://translate.terraprint.co/translate"
        
        # Supported languages
        self.supported_languages = {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'pt': 'Portuguese',
            'ru': 'Russian',
            'zh': 'Chinese',
            'ja': 'Japanese',
            'ko': 'Korean',
            'ar': 'Arabic',
            'hi': 'Hindi'
        }
    
    def translate(self, text, target_lang='en', source_lang='auto'):
        """
        Translate text to target language
        
        Args:
            text (str): Text to translate
            target_lang (str): Target language code (e.g., 'en', 'es', 'fr')
            source_lang (str): Source language code or 'auto' for auto-detection
            
        Returns:
            str: Translated text
        """
        if not text or target_lang == 'en' or target_lang not in self.supported_languages:
            return text
        
        try:
            # Prepare request data
            data = {
                'q': text,
                'source': source_lang,
                'target': target_lang,
                'format': 'text'
            }
            
            # Send request to API
            response = requests.post(self.api_url, json=data, timeout=10)
            
            # Check if request was successful
            if response.status_code == 200:
                result = response.json()
                if 'translatedText' in result:
                    return result['translatedText']
            
            # If anything fails, return original text
            return text
            
        except Exception as e:
            print(f"Translation failed: {str(e)}")
            return text