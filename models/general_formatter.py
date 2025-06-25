import re

class GeneralFormatter:
    """A general text formatter that can handle any type of text with concatenated words"""
    
    @staticmethod
    def format_text(text):
        """Format text with proper spacing between words"""
        if not text:
            return ""
        
        # First, apply general formatting rules
        formatted_text = text
        
        # 1. Add spaces between lowercase and uppercase letters (camelCase)
        formatted_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', formatted_text)
        
        # 2. Add spaces between lowercase letters and digits
        formatted_text = re.sub(r'([a-z])(\d)', r'\1 \2', formatted_text)
        formatted_text = re.sub(r'(\d)([a-z])', r'\1 \2', formatted_text)
        
        # 3. Fix spacing after punctuation
        formatted_text = re.sub(r'\.([A-Za-z])', r'. \1', formatted_text)  # Period
        formatted_text = re.sub(r',([A-Za-z])', r', \1', formatted_text)   # Comma
        formatted_text = re.sub(r';([A-Za-z])', r'; \1', formatted_text)   # Semicolon
        formatted_text = re.sub(r':([A-Za-z])', r': \1', formatted_text)   # Colon
        formatted_text = re.sub(r'!([A-Za-z])', r'! \1', formatted_text)   # Exclamation
        formatted_text = re.sub(r'\?([A-Za-z])', r'? \1', formatted_text)  # Question mark
        
        # 4. Fix spacing around parentheses and brackets
        formatted_text = re.sub(r'([A-Za-z])(\()', r'\1 \2', formatted_text)
        formatted_text = re.sub(r'(\))([A-Za-z])', r'\1 \2', formatted_text)
        
        # 5. Fix common word concatenations by looking for common patterns
        # This uses a sliding window approach to find potential word boundaries
        words = formatted_text.split()
        processed_words = []
        
        for word in words:
            # Skip short words
            if len(word) <= 5:
                processed_words.append(word)
                continue
                
            # Check if this is likely a concatenated word
            is_concatenated = False
            
            # Look for common word boundaries (vowel followed by consonant)
            for i in range(2, len(word) - 2):
                # Check if we have a vowel followed by a consonant
                if (word[i-1].lower() in 'aeiou' and 
                    word[i].lower() not in 'aeiou' and 
                    word[i+1].lower() not in 'aeiou'):
                    # Potential word boundary
                    part1 = word[:i]
                    part2 = word[i:]
                    
                    # Only split if both parts are reasonably sized
                    if len(part1) >= 2 and len(part2) >= 2:
                        processed_words.append(part1)
                        processed_words.append(part2)
                        is_concatenated = True
                        break
            
            # If not identified as concatenated, keep as is
            if not is_concatenated:
                processed_words.append(word)
        
        # Rejoin the words
        formatted_text = ' '.join(processed_words)
        
        # 6. Fix common prefixes and suffixes
        prefixes = ['re', 'pre', 'post', 'anti', 'auto', 'bi', 'co', 'counter', 'de', 'dis', 
                   'en', 'ex', 'extra', 'hyper', 'il', 'im', 'in', 'inter', 'intra', 'ir', 
                   'micro', 'mid', 'mis', 'non', 'over', 'poly', 'pro', 'pseudo', 'semi', 
                   'sub', 'super', 'trans', 'tri', 'ultra', 'un', 'under']
        
        for prefix in prefixes:
            formatted_text = re.sub(fr'\b{prefix}([a-z])', fr'{prefix}\1', formatted_text)
        
        # 7. Fix common word pairs that should be together
        common_pairs = [
            ('data', 'base'), ('key', 'word'), ('back', 'ground'), ('every', 'one'),
            ('some', 'one'), ('any', 'one'), ('no', 'one'), ('every', 'thing'),
            ('some', 'thing'), ('any', 'thing'), ('no', 'thing'), ('web', 'site'),
            ('data', 'set'), ('time', 'stamp'), ('life', 'style'), ('life', 'time'),
            ('work', 'flow'), ('feed', 'back'), ('frame', 'work'), ('open', 'source'),
            ('data', 'type'), ('use', 'case'), ('end', 'point'), ('data', 'structure'),
            ('source', 'code'), ('object', 'oriented'), ('machine', 'learning'),
            ('deep', 'learning'), ('natural', 'language'), ('computer', 'vision'),
            ('artificial', 'intelligence'), ('neural', 'network'), ('big', 'data'),
            ('cloud', 'computing'), ('internet', 'things'), ('block', 'chain'),
            ('cyber', 'security'), ('information', 'technology'), ('software', 'development'),
            ('data', 'science'), ('user', 'interface'), ('user', 'experience'),
            ('front', 'end'), ('back', 'end'), ('full', 'stack'), ('real', 'time'),
            ('high', 'level'), ('low', 'level'), ('cross', 'platform'), ('open', 'source'),
            ('version', 'control'), ('continuous', 'integration'), ('continuous', 'deployment'),
            ('test', 'driven'), ('agile', 'development'), ('waterfall', 'model'),
            ('technical', 'debt'), ('code', 'review'), ('pair', 'programming'),
            ('extreme', 'programming'), ('functional', 'programming'), ('object', 'oriented'),
            ('design', 'pattern'), ('anti', 'pattern'), ('code', 'smell'),
            ('refactoring', 'code'), ('legacy', 'code'), ('clean', 'code'),
            ('technical', 'documentation'), ('unit', 'test'), ('integration', 'test'),
            ('regression', 'test'), ('acceptance', 'test'), ('performance', 'test'),
            ('load', 'test'), ('stress', 'test'), ('security', 'test'),
            ('penetration', 'test'), ('white', 'box'), ('black', 'box'),
            ('gray', 'box'), ('test', 'case'), ('test', 'suite'),
            ('test', 'plan'), ('test', 'strategy'), ('test', 'coverage'),
            ('code', 'coverage'), ('bug', 'tracking'), ('issue', 'tracking'),
            ('version', 'control'), ('source', 'control'), ('git', 'hub'),
            ('bit', 'bucket'), ('git', 'lab'), ('continuous', 'integration'),
            ('continuous', 'delivery'), ('continuous', 'deployment'),
            ('dev', 'ops'), ('site', 'reliability'), ('infrastructure', 'code'),
            ('configuration', 'management'), ('container', 'orchestration'),
            ('micro', 'services'), ('service', 'oriented'), ('event', 'driven'),
            ('domain', 'driven'), ('test', 'driven'), ('behavior', 'driven'),
            ('data', 'driven'), ('user', 'centered'), ('mobile', 'first'),
            ('responsive', 'design'), ('progressive', 'enhancement'),
            ('graceful', 'degradation'), ('single', 'page'), ('progressive', 'web'),
            ('native', 'app'), ('hybrid', 'app'), ('cross', 'platform'),
            ('real', 'time'), ('batch', 'processing'), ('stream', 'processing'),
            ('big', 'data'), ('data', 'mining'), ('machine', 'learning'),
            ('deep', 'learning'), ('neural', 'network'), ('natural', 'language'),
            ('computer', 'vision'), ('artificial', 'intelligence'),
            ('expert', 'system'), ('knowledge', 'base'), ('data', 'warehouse'),
            ('business', 'intelligence'), ('decision', 'support'),
            ('predictive', 'analytics'), ('prescriptive', 'analytics'),
            ('descriptive', 'analytics'), ('diagnostic', 'analytics'),
            ('data', 'visualization'), ('information', 'architecture'),
            ('user', 'experience'), ('user', 'interface'), ('user', 'research'),
            ('usability', 'testing'), ('accessibility', 'testing'),
            ('human', 'computer'), ('interaction', 'design'), ('visual', 'design'),
            ('information', 'design'), ('experience', 'design'), ('service', 'design'),
            ('product', 'design'), ('industrial', 'design'), ('graphic', 'design'),
            ('web', 'design'), ('mobile', 'design'), ('responsive', 'design'),
            ('adaptive', 'design'), ('material', 'design'), ('flat', 'design'),
            ('skeuomorphic', 'design'), ('minimalist', 'design'), ('brutalist', 'design')
        ]
        
        for word1, word2 in common_pairs:
            formatted_text = re.sub(fr'\b{word1}\s+{word2}\b', f'{word1}{word2}', formatted_text)
            formatted_text = re.sub(fr'\b{word1}{word2}\b', f'{word1} {word2}', formatted_text)
        
        # 8. Remove excessive whitespace
        formatted_text = re.sub(r'\s{2,}', ' ', formatted_text)
        
        return formatted_text.strip()
    
    @staticmethod
    def format_keywords(keywords):
        """Format keywords with proper spacing"""
        formatted_keywords = []
        
        for keyword in keywords:
            term = keyword["term"]
            score = keyword["score"]
            
            # Format the term
            formatted_term = GeneralFormatter.format_text(term)
            
            # Add to formatted keywords
            formatted_keywords.append({
                "term": formatted_term,
                "score": score
            })
        
        return formatted_keywords