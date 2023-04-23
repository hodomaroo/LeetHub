class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(index : int) -> int:
            if index == len(s): return 1
            if s[index] == "0": return 0
            value,_return = 0,0
            
            for i in range(index, min(len(s), index + 11)):
                value = value * 10 + int(s[i])
                if 1 <= value <= k:
                    _return = (_return + dfs(i + 1)) % MOD
            return _return 
        
        return dfs(0)
                    
                
            