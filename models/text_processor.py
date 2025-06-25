import re

class TextProcessor:
    """A simple text processor to fix spacing and formatting issues"""
    
    @staticmethod
    def fix_spacing(text):
        """Fix spacing issues in text"""
        if not text:
            return ""
            
        # First, add spaces between words that are concatenated
        # This handles cases like "dataanddecision" -> "data and decision"
        
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
        processed_text = text
        for i, word1 in enumerate(common_words):
            for word2 in common_words:
                if word1 != word2:
                    pattern = f"({word1})({word2})"
                    processed_text = re.sub(pattern, r"\1 \2", processed_text, flags=re.IGNORECASE)
        
        # Add spaces between lowercase and uppercase letters (camelCase)
        processed_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', processed_text)
        
        # Add spaces after periods that aren't followed by space
        processed_text = re.sub(r'\.([A-Za-z])', r'. \1', processed_text)
        
        # Add spaces after commas that aren't followed by space
        processed_text = re.sub(r',([A-Za-z])', r', \1', processed_text)
        
        # Fix spacing between sentences
        processed_text = re.sub(r'([.!?])([A-Z])', r'\1 \2', processed_text)
        
        # Fix spacing and punctuation
        processed_text = re.sub(r'\s+-\s*\.', r'.', processed_text)  # Remove "- ."
        processed_text = re.sub(r'\s+\.', r'.', processed_text)  # Fix spaces before periods
        
        # Remove excessive whitespace
        processed_text = re.sub(r'\s{2,}', ' ', processed_text)
        
        return processed_text.strip()
    
    @staticmethod
    def format_topic_terms(terms):
        """Format topic terms with proper spacing"""
        if not terms:
            return []
            
        formatted_terms = []
        for term in terms:
            # Add spaces between lowercase and uppercase letters
            term = re.sub(r'([a-z])([A-Z])', r'\1 \2', term)
            
            # Add spaces between common words
            common_words = ["blockchain", "technology", "data", "decision", "systems"]
            for word in common_words:
                pattern = f"({word})"
                term = re.sub(pattern, r" \1 ", term, flags=re.IGNORECASE)
            
            # Remove excessive whitespace
            term = re.sub(r'\s{2,}', ' ', term).strip()
            
            formatted_terms.append(term)
            
        return formatted_terms
    
    @staticmethod
    def extract_keywords(text, num_keywords=20):
        """Extract meaningful keywords from text"""
        # Clean the text
        text = TextProcessor.fix_spacing(text)
        
        # Split into words
        words = text.split()
        
        # Common words to exclude
        stop_words = {
            'the', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'by',
            'of', 'that', 'this', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
            'can', 'could', 'may', 'might', 'must', 'from', 'as', 'if', 'then', 'than'
        }
        
        # Filter out stop words and short words
        filtered_words = [word for word in words if word.lower() not in stop_words and len(word) > 3]
        
        # Extract important technical terms
        technical_terms = [
            "blockchain", "technology", "decentralized", "distributed", "consensus",
            "transaction", "ledger", "hash", "security", "network", "node", "client",
            "application", "process", "database", "block", "public", "private", "key",
            "infrastructure", "smart", "contract", "proof", "work", "stake", "ethereum",
            "bitcoin", "hyperledger", "fabric", "sawtooth", "quorum", "permissioned",
            "permissionless", "consortium", "immutable", "cryptography", "encryption"
        ]
        
        # Create keywords with scores
        keywords = []
        
        # First add technical terms that appear in the text
        for term in technical_terms:
            if term.lower() in [word.lower() for word in filtered_words]:
                keywords.append({"term": term, "score": 1.0})
        
        # Then add other frequent words
        from collections import Counter
        word_counts = Counter(filtered_words)
        
        # Get the most common words
        for word, count in word_counts.most_common(num_keywords):
            if len(keywords) >= num_keywords:
                break
                
            # Skip if already added
            if any(keyword["term"].lower() == word.lower() for keyword in keywords):
                continue
                
            keywords.append({"term": word, "score": count / len(filtered_words)})
        
        return keywords[:num_keywords]