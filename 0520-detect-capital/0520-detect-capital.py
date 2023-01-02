class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in [word.lower(), word.upper(), word[0].upper() + word[1:].lower()]
        
        