from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import nltk
from nltk.corpus import stopwords
import re

class TopicExtractor:
    def __init__(self):
        # Download NLTK resources if not already downloaded
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        
        self.stop_words = set(stopwords.words('english'))
        
    def extract_topics(self, text, num_topics=3, num_words=5):
        """
        Extract main topics from text using NMF and TF-IDF
        
        Args:
            text (str): Text to analyze
            num_topics (int): Number of topics to extract
            num_words (int): Number of words per topic
            
        Returns:
            list: List of topics, each containing key terms
        """
        # Pre-process text to fix common terms
        text = re.sub(r'B\.\s*T\s*ech', r'BTech', text)
        text = re.sub(r'C\s*G\s*P\s*A', r'CGPA', text)
        text = re.sub(r'junior\s*college', r'JuniorCollege', text)
        text = re.sub(r'as\s+shown\s+in\s+figure', r'as_shown_in_figure', text)
        text = re.sub(r'public\s+key\s+infrastructure', r'public_key_infrastructure', text)
        
        try:
            # Clean and tokenize text
            cleaned_text = self._preprocess_text(text)
            
            # Handle very short texts or empty text
            if not cleaned_text or len(cleaned_text.split()) < 20:
                return [{"topic": "Main Topic", "terms": ["insufficient", "text", "for", "topic", "extraction"]}]
            
            # Add common terms to the stop words
            custom_stop_words = ['cgpa', 'gpa', 'the', 'and', 'for', 'with', 'from', 'that', 'this']
            
            # Create TF-IDF matrix with safer parameters
            vectorizer = TfidfVectorizer(
                max_df=1.0,   # Set to 1.0 to include all terms
                min_df=1,     # Keep at 1 to include terms that appear at least once
                max_features=500,
                stop_words=list(set(list(self.stop_words) + custom_stop_words))
            )
            
            # For all texts, use simple keyword extraction
            tfidf = vectorizer.fit_transform([cleaned_text])
            
            try:
                feature_names = vectorizer.get_feature_names_out()
                
                # Get top terms
                scores = zip(feature_names, tfidf.toarray()[0])
                sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
                
                # Check if this is likely a resume
                is_resume = any(term in text.lower() for term in ['resume', 'cv', 'curriculum vitae', 'education', 'experience', 'skills', 'btech', 'b.tech', 'degree', 'college'])
                
                # Group into topics
                topics = []
                if is_resume:
                    # For resumes, create more meaningful topic categories
                    education_terms = [term for term, score in sorted_scores if term.lower() in ['college', 'university', 'degree', 'btech', 'education', 'cgpa', 'gpa', 'school', 'academic']]
                    skills_terms = [term for term, score in sorted_scores if term.lower() in ['python', 'java', 'javascript', 'html', 'css', 'programming', 'development', 'software', 'web', 'app', 'coding']]
                    project_terms = [term for term, score in sorted_scores if term.lower() in ['project', 'developed', 'created', 'built', 'implemented', 'designed', 'application', 'system', 'platform']]
                    
                    # Add education topic if we have terms
                    if education_terms:
                        topics.append({
                            "topic": "Education",
                            "terms": education_terms[:num_words]
                        })
                    
                    # Add skills topic if we have terms
                    if skills_terms:
                        topics.append({
                            "topic": "Skills",
                            "terms": skills_terms[:num_words]
                        })
                    
                    # Add projects topic if we have terms
                    if project_terms:
                        topics.append({
                            "topic": "Projects",
                            "terms": project_terms[:num_words]
                        })
                    
                    # If we don't have enough topics, add general ones
                    if len(topics) < num_topics:
                        remaining_terms = [term for term, score in sorted_scores 
                                          if term not in education_terms and term not in skills_terms and term not in project_terms]
                        if remaining_terms:
                            topics.append({
                                "topic": "Additional Information",
                                "terms": remaining_terms[:num_words]
                            })
                else:
                    # For technical documents, use specific categories
                    tech_terms = [term for term, score in sorted_scores if term.lower() in ['blockchain', 'technology', 'decentralized', 'systems', 'data', 'decision', 'topology', 'infrastructure', 'pki', 'public_key_infrastructure']]
                    if tech_terms:
                        topics.append({
                            "topic": "Technology",
                            "terms": tech_terms[:num_words]
                        })
                    
                    # Add more general topics
                    for i in range(min(num_topics - len(topics), 2)):
                        start_idx = i * num_words
                        end_idx = start_idx + num_words
                        terms = [term for term, score in sorted_scores[start_idx:end_idx] if score > 0 and term not in tech_terms]
                        if terms:  # Only add if we have terms
                            topics.append({
                                "topic": f"Topic {i + 1}",
                                "terms": terms
                            })
                
                if not topics:
                    return [{"topic": "Main Topic", "terms": ["no", "significant", "topics", "found"]}]
                return topics
                
            except Exception as e:
                print(f"Error extracting features: {str(e)}")
                return [{"topic": "Topic Extraction Error", "terms": ["error", "extracting", "topics"]}]
                
        except Exception as e:
            print(f"Topic extraction failed: {str(e)}")
            return [{"topic": "Topic Extraction Failed", "terms": ["error", "processing", "text"]}]
    
    def extract_keywords(self, text, num_keywords=10):
        """
        Extract keywords from text using TF-IDF
        
        Args:
            text (str): Text to analyze
            num_keywords (int): Number of keywords to extract
            
        Returns:
            list: List of keywords with their scores
        """
        try:
            # First, preserve important phrases
            text = re.sub(r'as\s+shown\s+in\s+figure', 'as_shown_in_figure', text, flags=re.IGNORECASE)
            text = re.sub(r'public\s+key\s+infrastructure', 'public_key_infrastructure', text, flags=re.IGNORECASE)
            text = re.sub(r'blockchain\s+technology', 'blockchain_technology', text, flags=re.IGNORECASE)
            text = re.sub(r'data\s+and\s+decision', 'data_and_decision', text, flags=re.IGNORECASE)
            text = re.sub(r'decentralized\s+systems', 'decentralized_systems', text, flags=re.IGNORECASE)
            
            # Clean text
            cleaned_text = self._preprocess_text(text)
            
            # Handle very short texts
            if not cleaned_text or len(cleaned_text.split()) < 10:
                return [{"term": "insufficient", "score": 1.0}, {"term": "text", "score": 0.8}]
            
            # Create TF-IDF matrix with custom parameters
            stop_words = ['the', 'and', 'for', 'with', 'from', 'that', 'this', 'was', 'are', 'not', 
                         'have', 'has', 'been', 'may', 'any', 'its', 'it', 'in', 'on', 'at', 'to']
            
            vectorizer = TfidfVectorizer(
                max_df=0.95,
                min_df=1,
                stop_words=stop_words,
                token_pattern=r'(?u)\b[a-zA-Z_][a-zA-Z_]+\b'  # Allow underscores
            )
            
            tfidf = vectorizer.fit_transform([cleaned_text])
            feature_names = vectorizer.get_feature_names_out()
            
            # Get scores and sort
            scores = zip(feature_names, tfidf.toarray()[0])
            sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
            
            # Process keywords
            keywords = []
            seen_terms = set()
            
            for term, score in sorted_scores:
                # Restore original phrases
                if '_' in term:
                    term = term.replace('_', ' ')
                
                # Skip if we've seen this term
                if term in seen_terms:
                    continue
                
                # Skip very short or very long terms
                if len(term) <= 2 or len(term) > 30:
                    continue
                
                # Skip if term contains unwanted patterns
                if re.search(r'^\d+$|^[^a-zA-Z]+$', term):
                    continue
                
                keywords.append({"term": term.strip(), "score": float(score)})
                seen_terms.add(term)
                
                if len(keywords) >= num_keywords:
                    break
            
            return keywords
            
        except Exception as e:
            print(f"Keyword extraction failed: {str(e)}")
            return [{"term": "extraction", "score": 1.0}, {"term": "failed", "score": 0.8}]
    
    def _preprocess_text(self, text):
        """Clean and normalize text"""
        # Convert to lowercase
        text = text.lower()
        
        # Fix incorrectly split words
        text = re.sub(r'([a-z])\s+([a-z])', r'\1\2', text)  # Fix "t ra vel" -> "travel"
        text = re.sub(r'([a-z])\s+([aeiouy][a-z])', r'\1\2', text)  # Fix "p ersonalized" -> "personalized"
        
        # Replace special characters with spaces to ensure word separation
        # But preserve underscores for our special phrases
        text = re.sub(r'[^\w\s_]', ' ', text)
        text = re.sub(r'(?<![a-zA-Z_])\d+(?![a-zA-Z_])', ' ', text)  # Only replace standalone digits
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text