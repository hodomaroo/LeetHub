class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            link = [-1] * 26
            rv_link = [-1] * 26
            flg = True
            
            for i in range(len(pattern)):
                fr,to = ord(word[i]) - ord("a"), ord(pattern[i]) - ord("a")
                
                if link[fr] == -1 and rv_link[to] == -1:
                    link[fr] = to
                    rv_link[to] = fr
                
                if not(link[fr] == to and rv_link[to] == fr):
                    flg = False
                    break
            if flg:
                ans.append(word)
        return ans
                
                    
                
                