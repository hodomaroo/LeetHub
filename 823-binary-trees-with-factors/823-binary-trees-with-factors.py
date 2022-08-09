class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        #만들 수 있는 곱의 조합
        MOD = 10 ** 9 + 7
        arr.sort()
        arrDict = {arr[i] : i for i in range(len(arr))}
        dp = [-1] * len(arr)
        
        def dfs(index : int) -> int: 
            if dp[index] >= 0:
                return dp[index]
            
            dp[index] = 1
            
            for i in range(index):
                if arr[index] % arr[i] or arr[index] // arr[i] not in arrDict: continue
                j = arrDict[arr[index] // arr[i]]
                
                if i != j:
                    add = dfs(i) * dfs(j)
                else:
                    add = dfs(i) * (dfs(i) - 1)  + dfs(i)
                    
                add %= MOD
                dp[index] = (dp[index] + add) % MOD           #양쪽이 동일할 때, 문제가 생김 -> 바꿔도.. 똑같은 트리..
            
                
            return dp[index]    
        
        ans = 0
        for i in range(len(arr)):
            ans = (dfs(i) + ans) % MOD
        
        return ans
            
                    
        
        
        