import re
from collections import Counter
import requests

class TextUtils:
    """Unified text utilities for processing, formatting, and summarizing text"""
    
    @staticmethod
    def fix_spacing(text):
        """Fix spacing issues in text"""
        if not text:
            return ""
            
        # Add spaces between lowercase and uppercase letters (camelCase)
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
        
        # Fix common concatenated words
        text = re.sub(r'([a-z]{2,})([A-Z][a-z]{2,})', r'\1 \2', text)
        
        # Add spaces after punctuation
        text = re.sub(r'\.([A-Za-z])', r'. \1', text)  # Period
        text = re.sub(r',([A-Za-z])', r', \1', text)   # Comma
        text = re.sub(r';([A-Za-z])', r'; \1', text)   # Semicolon
        text = re.sub(r':([A-Za-z])', r': \1', text)   # Colon
        
        # Fix spacing between sentences
        text = re.sub(r'([.!?])([A-Z])', r'\1 \2', text)
        
        # Fix common word patterns
        common_patterns = [
            (r'dataanddecision', r'data and decision'),
            (r'Indecentralizedsystems', r'In decentralized systems'),
            (r'thedataanddecisions', r'the data and decisions'),
            (r'Itmaybeanyexisting', r'It may be any existing'),
            (r'Clientsarerestrictedusing', r'Clients are restricted using'),
            (r'atblockchain', r'at blockchain'),
            (r'Thetopology', r'The topology'),
            (r'blockchaintechnology', r'blockchain technology'),
            (r'machinelearning', r'machine learning'),
            (r'artificialintelligence', r'artificial intelligence'),
            (r'computervision', r'computer vision'),
            (r'naturallanguage', r'natural language'),
            (r'deeplearning', r'deep learning'),
            (r'neuralnetwork', r'neural network'),
            (r'datascienc', r'data scienc')
        ]
        
        for pattern, replacement in common_patterns:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        # Remove excessive whitespace
        text = re.sub(r'\s{2,}', ' ', text)
        
        return text.strip()
    
    @staticmethod
    def extract_keywords(text, num_keywords=20):
        """Extract keywords from text"""
        # Clean the text
        text = TextUtils.fix_spacing(text)
        
        # Common words to exclude
        stop_words = {
            'the', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'by',
            'of', 'that', 'this', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
            'can', 'could', 'may', 'might', 'must', 'from', 'as', 'if', 'then', 'than'
        }
        
        # Split into words
        words = text.lower().split()
        
        # Filter out stop words and short words
        filtered_words = [word for word in words if word not in stop_words and len(word) > 3]
        
        # Count word frequencies
        word_counts = Counter(filtered_words)
        
        # Get the most common words
        keywords = []
        for word, count in word_counts.most_common(num_keywords):
            keywords.append({
                "term": word,
                "score": count / len(filtered_words)
            })
        
        return keywords
    
    @staticmethod
    def extract_topics(text, num_topics=3, num_words=10):
        """Extract topics from text"""
        # Clean the text
        text = TextUtils.fix_spacing(text)
        
        # Define topic categories and their associated terms
        topic_categories = {
            "Technology": [
                'blockchain', 'technology', 'decentralized', 'systems', 'data', 'decision', 
                'topology', 'infrastructure', 'security', 'network', 'algorithm', 'software', 
                'hardware', 'platform', 'application', 'system', 'digital', 'computer', 
                'internet', 'web', 'cloud', 'api', 'interface', 'protocol', 'encryption'
            ],
            "Business": [
                'business', 'company', 'organization', 'management', 'strategy', 'marketing',
                'sales', 'customer', 'client', 'product', 'service', 'market', 'industry',
                'revenue', 'profit', 'growth', 'startup', 'enterprise', 'corporation'
            ],
            "Education": [
                'education', 'learning', 'teaching', 'school', 'university', 'college',
                'student', 'teacher', 'professor', 'course', 'curriculum', 'degree',
                'academic', 'research', 'study', 'knowledge', 'skill', 'training'
            ],
            "Science": [
                'science', 'scientific', 'research', 'experiment', 'theory', 'hypothesis',
                'analysis', 'data', 'evidence', 'observation', 'laboratory', 'discovery',
                'innovation', 'development', 'advancement', 'breakthrough'
            ]
        }
        
        # Count occurrences of terms in each category
        topic_scores = {}
        for category, terms in topic_categories.items():
            score = 0
            for term in terms:
                score += text.lower().count(term)
            topic_scores[category] = score
        
        # Sort topics by score
        sorted_topics = sorted(topic_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Create topics with terms
        topics = []
        for category, score in sorted_topics[:num_topics]:
            if score > 0:
                # Find terms from this category that appear in the text
                terms = []
                for term in topic_categories[category]:
                    if term in text.lower() and len(terms) < num_words:
                        terms.append(term)
                
                # Only add topics with terms
                if terms:
                    topics.append({
                        "topic": category,
                        "terms": terms
                    })
        
        return topics
    
    @staticmethod
    def summarize_text(text, ratio=0.5):
        """Generate a summary by extracting key sentences"""
        # Clean the text
        text = TextUtils.fix_spacing(text)
        
        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
        
        # Handle very short texts
        if len(sentences) <= 3:
            return text
        
        # Calculate number of sentences to include
        num_sentences = max(1, int(len(sentences) * ratio))
        
        # For simplicity, take sentences from beginning, middle, and end
        selected_sentences = []
        
        # Always include the first sentence
        selected_sentences.append(sentences[0])
        
        # If we need more sentences, add from middle and end
        if num_sentences > 1:
            remaining = num_sentences - 1
            
            if remaining == 1:
                # Just take the last sentence
                selected_sentences.append(sentences[-1])
            elif remaining == 2:
                # Take one from middle and one from end
                middle_idx = len(sentences) // 2
                selected_sentences.append(sentences[middle_idx])
                selected_sentences.append(sentences[-1])
            else:
                # Distribute remaining sentences evenly
                step = len(sentences) // remaining
                for i in range(1, remaining):
                    idx = i * step
                    if idx < len(sentences) and idx not in [0, len(sentences)-1]:
                        selected_sentences.append(sentences[idx])
                
                # Always include the last sentence
                if sentences[-1] not in selected_sentences:
                    selected_sentences.append(sentences[-1])
        
        # Ensure we don't exceed the requested ratio
        selected_sentences = selected_sentences[:num_sentences]
        
        # Sort sentences by their original order
        sentence_indices = [(sentences.index(s), s) for s in selected_sentences]
        sentence_indices.sort()
        
        # Join the selected sentences
        summary = ' '.join([s[1] for s in sentence_indices])
        
        # Ensure the summary ends with proper punctuation
        if summary and not summary.rstrip().endswith(('.', '!', '?')):
            summary = summary.rstrip() + "."
        
        return summary
    
    @staticmethod
    def translate_text(text, target_lang='en'):
        """Translate text to target language"""
        if not text or target_lang == 'en':
            return text
        
        try:
            # Use LibreTranslate API
            api_url = "https://translate.terraprint.co/translate"
            
            data = {
                'q': text,
                'source': 'auto',
                'target': target_lang,
                'format': 'text'
            }
            
            response = requests.post(api_url, json=data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                if 'translatedText' in result:
                    return result['translatedText']
            
            return text
            
        except Exception as e:
            print(f"Translation failed: {str(e)}")
            return text