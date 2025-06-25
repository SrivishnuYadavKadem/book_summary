import re

class SimpleSummarizer:
    """A simple extractive summarizer that doesn't rely on external libraries"""
    
    def summarize(self, text, ratio=0.5):
        """
        Generate a summary by extracting sentences from the text
        
        Args:
            text (str): Text to summarize
            ratio (float): Proportion of sentences to keep (0.0-1.0)
            
        Returns:
            str: Extractive summary
        """
        # Clean the text
        text = self._clean_text(text)
        
        # Split into sentences
        sentences = self._split_into_sentences(text)
        
        # Handle very short texts
        if len(sentences) <= 3:
            return text
        
        # Calculate number of sentences to include
        num_sentences = max(1, int(len(sentences) * ratio))
        
        # For simplicity, just take sentences from the beginning, middle, and end
        selected_sentences = []
        
        # Always include the first sentence (introduction)
        selected_sentences.append(sentences[0])
        
        # If we need more sentences, add from middle and end
        if num_sentences > 1:
            # Calculate how many sentences to take from each section
            remaining = num_sentences - 1  # Already took first sentence
            
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
                
                # Always include the last sentence (conclusion)
                if sentences[-1] not in selected_sentences:
                    selected_sentences.append(sentences[-1])
        
        # Ensure we don't exceed the requested ratio
        selected_sentences = selected_sentences[:num_sentences]
        
        # Sort sentences by their original order
        sentence_indices = [(sentences.index(s), s) for s in selected_sentences]
        sentence_indices.sort()
        
        # Join the selected sentences
        summary = ' '.join([s[1] for s in sentence_indices])
        
        return summary
    
    def _clean_text(self, text):
        """Clean the text for better sentence splitting"""
        # Fix common formatting issues
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
        text = re.sub(r'\n+', ' ', text)  # Replace newlines with spaces
        
        # Common word boundaries to check
        common_words = [
            "blockchain", "technology", "data", "decision", "systems", 
            "public", "key", "infrastructure", "network", "transaction",
            "consensus", "node", "client", "application", "process",
            "database", "ledger", "block", "hash", "security",
            "distributed", "decentralized", "centralized", "figure",
            "shown", "topology", "platform", "hyperledger", "ethereum",
            "bitcoin", "smart", "contract", "proof", "work", "stake",
            "private", "consortium", "permissioned", "permissionless"
        ]
        
        # Add spaces between common words
        for i, word1 in enumerate(common_words):
            for word2 in common_words:
                if word1 != word2:
                    pattern = f"({word1})({word2})"
                    text = re.sub(pattern, r"\1 \2", text, flags=re.IGNORECASE)
        
        # Add spaces between lowercase and uppercase letters (camelCase)
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
        
        # Add spaces after periods that aren't followed by space
        text = re.sub(r'\.([A-Za-z])', r'. \1', text)
        
        # Add spaces after commas that aren't followed by space
        text = re.sub(r',([A-Za-z])', r', \1', text)
        
        # Fix spacing between sentences
        text = re.sub(r'([.!?])([A-Z])', r'\1 \2', text)
        
        # Fix specific concatenated words
        text = re.sub(r'dataanddecision', r'data and decision', text)
        text = re.sub(r'Indecentralizedsystems', r'In decentralized systems', text)
        text = re.sub(r'thedataanddecisions', r'the data and decisions', text)
        text = re.sub(r'Itmaybeanyexistingapplication', r'It may be any existing application', text)
        text = re.sub(r'Clientsarerestrictedusing', r'Clients are restricted using', text)
        text = re.sub(r'atblockchain', r'at blockchain', text)
        text = re.sub(r'Thetopology', r'The topology', text)
        text = re.sub(r'thedata anddecision', r'the data and decision', text)
        text = re.sub(r'asshownin', r'as shown in', text)
        
        return text.strip()
    
    def _split_into_sentences(self, text):
        """Split text into sentences using regex"""
        # Simple sentence splitting using regex
        # This handles common sentence endings (., !, ?) followed by a space and capital letter
        sentence_endings = r'(?<=[.!?])\s+(?=[A-Z])'
        sentences = re.split(sentence_endings, text)
        
        # Filter out empty sentences
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return sentences