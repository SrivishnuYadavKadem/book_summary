import re
from collections import Counter

class SimpleKeywordExtractor:
    """A simple keyword extractor that doesn't rely on TF-IDF"""
    
    def __init__(self):
        # Common words to exclude
        self.stop_words = {
            'the', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'by',
            'of', 'that', 'this', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
            'can', 'could', 'may', 'might', 'must', 'from', 'as', 'if', 'then', 'than',
            'so', 'such', 'what', 'who', 'when', 'where', 'which', 'how', 'why',
            'or', 'not', 'no', 'nor', 'but', 'because', 'although', 'though',
            'while', 'during', 'through', 'throughout', 'therefore', 'thus', 'hence',
            'however', 'nevertheless', 'nonetheless', 'consequently', 'accordingly',
            'its', 'it', 'they', 'them', 'their', 'he', 'him', 'his', 'she', 'her',
            'we', 'us', 'our', 'you', 'your', 'i', 'me', 'my', 'mine', 'yours', 'ours',
            'about', 'above', 'across', 'after', 'against', 'along', 'among', 'around',
            'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond',
            'into', 'like', 'near', 'off', 'onto', 'out', 'over', 'under', 'up', 'upon',
            'within', 'without'
        }
    
    def extract_keywords(self, text, num_keywords=20):
        """
        Extract keywords from text using frequency analysis
        
        Args:
            text (str): Text to analyze
            num_keywords (int): Number of keywords to extract (default: 20)
            
        Returns:
            list: List of keywords with their scores
        """
        try:
            # Clean the text
            cleaned_text = self._clean_text(text)
            
            # Extract phrases (2-3 word combinations)
            phrases = self._extract_phrases(cleaned_text)
            
            # Extract single words
            words = self._extract_words(cleaned_text)
            
            # Combine phrases and words, prioritizing phrases
            all_terms = []
            
            # Add top phrases first (they're more meaningful)
            for phrase, count in phrases.most_common(num_keywords // 2):
                all_terms.append({"term": phrase, "score": count / len(phrases)})
            
            # Add top words to fill the remaining slots
            remaining = num_keywords - len(all_terms)
            for word, count in words.most_common(remaining):
                all_terms.append({"term": word, "score": count / len(words)})
            
            # Normalize scores to 0-1 range
            max_score = max([term["score"] for term in all_terms]) if all_terms else 1.0
            for term in all_terms:
                term["score"] = term["score"] / max_score
            
            return all_terms
            
        except Exception as e:
            print(f"Simple keyword extraction failed: {str(e)}")
            return [{"term": "extraction", "score": 1.0}, {"term": "failed", "score": 0.8}]
    
    def _clean_text(self, text):
        """Clean text for keyword extraction"""
        # Convert to lowercase
        text = text.lower()
        
        # Replace special characters with spaces
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Fix common formatting issues
        text = re.sub(r'([a-z])\s+([a-z])', r'\1\2', text)  # Fix split words
        
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def _extract_words(self, text):
        """Extract single words from text"""
        words = text.split()
        
        # Filter out stop words and short words
        filtered_words = [word for word in words if word not in self.stop_words and len(word) > 2]
        
        # Count word frequencies
        word_counts = Counter(filtered_words)
        
        return word_counts
    
    def _extract_phrases(self, text):
        """Extract meaningful phrases (2-3 word combinations)"""
        words = text.split()
        phrases = []
        
        # Extract 2-word phrases
        for i in range(len(words) - 1):
            if words[i] not in self.stop_words and words[i+1] not in self.stop_words:
                if len(words[i]) > 2 and len(words[i+1]) > 2:
                    phrases.append(f"{words[i]} {words[i+1]}")
        
        # Extract 3-word phrases
        for i in range(len(words) - 2):
            if words[i] not in self.stop_words and words[i+2] not in self.stop_words:
                if len(words[i]) > 2 and len(words[i+2]) > 2:
                    phrases.append(f"{words[i]} {words[i+1]} {words[i+2]}")
        
        # Count phrase frequencies
        phrase_counts = Counter(phrases)
        
        return phrase_counts