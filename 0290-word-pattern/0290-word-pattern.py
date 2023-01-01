class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        convert = dict()
        invert = dict()
        
        if len(pattern) != len(s.split(" ")):
            return False
        
        for pat,word in zip(list(pattern), s.split(" ")):
            if pat not in convert: 
                convert[pat] = word
            
            if word not in invert:
                invert[word] = pat
            
            
            if pat in convert and convert[pat] != word:
                return False
            
            if word in invert and invert[word] != pat:
                return False
        
        return True
                