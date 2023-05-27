class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        prefix = list(accumulate(stoneValue))
        
        
        @lru_cache(None)
        def dfs(index : int) -> int:
            if index == len(prefix): return 0
            
            return prefix[-1] - (prefix[index - 1] if index else 0) - min(dfs(nextIndex + 1) for nextIndex in range(index, min(index + 3, len(stoneValue))))
        
        res = dfs(0)
        return "Tie" if prefix[-1] / 2 == res else ["Bob","Alice"][res > prefix[-1] / 2]
                
                
                
        