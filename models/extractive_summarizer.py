import re
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np

class ExtractiveSummarizer:
    def __init__(self):
        # Download NLTK resources if not already downloaded
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('punkt', quiet=True)
            nltk.download('stopwords', quiet=True)
        
        self.stop_words = set(stopwords.words('english'))
    
    def summarize(self, text, ratio=0.5):
        """
        Generate an extractive summary of the text
        
        Args:
            text (str): Text to summarize
            ratio (float): Proportion of sentences to keep (0.0-1.0)
            
        Returns:
            str: Extractive summary
        """
        # Clean and preprocess text
        cleaned_text = self._clean_text(text)
        
        # Split text into sentences
        sentences = sent_tokenize(cleaned_text)
        
        # Handle very short texts
        if len(sentences) <= 3:
            return text
        
        # Calculate sentence similarity matrix
        similarity_matrix = self._build_similarity_matrix(sentences)
        
        # Rank sentences using PageRank algorithm
        sentence_scores = self._page_rank(similarity_matrix)
        
        # Calculate number of sentences to include
        num_sentences = max(1, int(len(sentences) * ratio))
        
        # Get top ranked sentences
        ranked_sentences = [sentences[i] for i in np.argsort(sentence_scores)[-num_sentences:]]
        
        # Sort sentences by their original order
        original_order = []
        for sentence in ranked_sentences:
            original_order.append((sentences.index(sentence), sentence))
        
        original_order.sort()
        summary = ' '.join([s[1] for s in original_order])
        
        return summary
    
    def _clean_text(self, text):
        """Clean and normalize text"""
        # Remove special characters and digits
        text = re.sub(r'[^\w\s.]', ' ', text)
        
        # Fix common formatting issues
        text = re.sub(r'([a-z])\s+([a-z])', r'\1\2', text)  # Fix split words
        text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
        
        return text
    
    def _sentence_similarity(self, sent1, sent2):
        """Calculate similarity between two sentences"""
        # Tokenize and convert to lowercase
        words1 = [word.lower() for word in nltk.word_tokenize(sent1)]
        words2 = [word.lower() for word in nltk.word_tokenize(sent2)]
        
        # Remove stop words
        words1 = [word for word in words1 if word not in self.stop_words]
        words2 = [word for word in words2 if word not in self.stop_words]
        
        # Create a set of all unique words
        all_words = list(set(words1 + words2))
        
        # Create word vectors
        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)
        
        # Fill vectors
        for word in words1:
            if word in all_words:
                vector1[all_words.index(word)] += 1
        
        for word in words2:
            if word in all_words:
                vector2[all_words.index(word)] += 1
        
        # Handle empty vectors
        if sum(vector1) == 0 or sum(vector2) == 0:
            return 0.0
        
        # Calculate cosine similarity
        return 1 - cosine_distance(vector1, vector2)
    
    def _build_similarity_matrix(self, sentences):
        """Build similarity matrix for all sentences"""
        # Initialize similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))
        
        # Fill similarity matrix
        for i in range(len(sentences)):
            for j in range(len(sentences)):
                if i != j:
                    similarity_matrix[i][j] = self._sentence_similarity(sentences[i], sentences[j])
        
        return similarity_matrix
    
    def _page_rank(self, similarity_matrix, damping=0.85, max_iter=100, tol=1e-5):
        """Implement PageRank algorithm to rank sentences"""
        n = len(similarity_matrix)
        
        # Normalize similarity matrix by row
        for i in range(n):
            row_sum = similarity_matrix[i].sum()
            if row_sum > 0:
                similarity_matrix[i] = similarity_matrix[i] / row_sum
        
        # Initialize scores
        scores = np.ones(n) / n
        
        # Power iteration
        for _ in range(max_iter):
            prev_scores = scores.copy()
            scores = (1 - damping) / n + damping * (similarity_matrix.T @ scores)
            
            # Check convergence
            if np.abs(scores - prev_scores).sum() < tol:
                break
        
        return scores