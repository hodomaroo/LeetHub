class Solution:
    def minInsertions(self, s: str) -> int:
        lca = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[-j - 1]:   lca[i][j] = 1 if not(i and j) else lca[i - 1][j - 1] + 1
                
                else:   lca[i][j] = max(lca[i-1][j] if i else 0, lca[i][j-1] if j else 0)
        
        return len(s) - lca[-1][-1]
                    
            



