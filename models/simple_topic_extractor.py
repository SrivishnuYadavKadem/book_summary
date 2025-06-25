import re
from collections import Counter

class SimpleTopicExtractor:
    """A simple topic extractor that doesn't rely on NMF or TF-IDF"""
    
    def __init__(self):
        # Common words to exclude
        self.stop_words = {
            'the', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'by',
            'of', 'that', 'this', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
            'can', 'could', 'may', 'might', 'must', 'from', 'as', 'if', 'then', 'than',
            'so', 'such', 'what', 'who', 'when', 'where', 'which', 'how', 'why'
        }
        
        # Define topic categories and their associated terms
        self.topic_categories = {
            "Technology": [
                'blockchain', 'technology', 'decentralized', 'systems', 'data', 'decision', 
                'topology', 'infrastructure', 'pki', 'public key', 'security', 'network',
                'algorithm', 'software', 'hardware', 'platform', 'application', 'system',
                'digital', 'computer', 'internet', 'web', 'cloud', 'api', 'interface',
                'protocol', 'encryption', 'authentication', 'authorization', 'distributed'
            ],
            "Education": [
                'college', 'university', 'degree', 'btech', 'education', 'cgpa', 'gpa', 
                'school', 'academic', 'course', 'study', 'student', 'professor', 'teacher',
                'learning', 'curriculum', 'semester', 'grade', 'graduation', 'bachelor',
                'master', 'phd', 'doctorate', 'thesis', 'research', 'project', 'assignment'
            ],
            "Skills": [
                'python', 'java', 'javascript', 'html', 'css', 'programming', 'development',
                'software', 'web', 'app', 'coding', 'framework', 'library', 'api', 'database',
                'sql', 'nosql', 'frontend', 'backend', 'fullstack', 'devops', 'cloud',
                'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'ci/cd', 'git', 'agile'
            ],
            "Business": [
                'business', 'company', 'organization', 'management', 'strategy', 'marketing',
                'sales', 'customer', 'client', 'product', 'service', 'market', 'industry',
                'revenue', 'profit', 'growth', 'startup', 'enterprise', 'corporation',
                'finance', 'investment', 'budget', 'cost', 'price', 'value', 'roi'
            ]
        }
    
    def extract_topics(self, text, num_topics=3, num_words=10):
        """
        Extract main topics from text
        
        Args:
            text (str): Text to analyze
            num_topics (int): Number of topics to extract
            num_words (int): Number of words per topic (default: 10)
            
        Returns:
            list: List of topics, each containing key terms
        """
        try:
            # Clean the text
            cleaned_text = self._clean_text(text)
            
            # Extract all words
            words = cleaned_text.split()
            
            # Filter out stop words and short words
            filtered_words = [word for word in words if word not in self.stop_words and len(word) > 2]
            
            # Count word frequencies
            word_counts = Counter(filtered_words)
            
            # Categorize words into topics
            topic_matches = {}
            for category, category_terms in self.topic_categories.items():
                # Find words that match this category
                matches = []
                for word, count in word_counts.items():
                    # Check if the word is in the category terms or contains any category term
                    if word in category_terms or any(term in word for term in category_terms):
                        matches.append((word, count))
                
                # Sort matches by frequency
                matches.sort(key=lambda x: x[1], reverse=True)
                
                # Store the top matches
                if matches:
                    topic_matches[category] = [word for word, _ in matches[:num_words]]
            
            # Create topics from matches
            topics = []
            for category, terms in topic_matches.items():
                if terms:  # Only add if we have terms
                    topics.append({
                        "topic": category,
                        "terms": terms
                    })
            
            # If we don't have enough topics, add general ones
            if len(topics) < num_topics:
                # Get the most common words that aren't already in a topic
                used_terms = set()
                for topic in topics:
                    used_terms.update(topic["terms"])
                
                remaining_words = [(word, count) for word, count in word_counts.items() if word not in used_terms]
                remaining_words.sort(key=lambda x: x[1], reverse=True)
                
                if remaining_words:
                    topics.append({
                        "topic": "General",
                        "terms": [word for word, _ in remaining_words[:num_words]]
                    })
            
            # Limit to the requested number of topics
            topics = topics[:num_topics]
            
            # If we still don't have any topics, return a default one
            if not topics:
                return [{"topic": "Main Topic", "terms": ["no", "significant", "topics", "found"]}]
            
            return topics
            
        except Exception as e:
            print(f"Simple topic extraction failed: {str(e)}")
            return [{"topic": "Topic Extraction Failed", "terms": ["error", "processing", "text"]}]
    
    def _clean_text(self, text):
        """Clean text for topic extraction"""
        # Convert to lowercase
        text = text.lower()
        
        # Replace special characters with spaces
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Fix common formatting issues
        text = re.sub(r'([a-z])\s+([a-z])', r'\1\2', text)  # Fix split words
        
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text