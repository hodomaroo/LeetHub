class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue = deque([0])
        valNodeMap = defaultdict(list)
        
        for i in range(len(arr)):
            valNodeMap[arr[i]].append(i)
            
        dp = [float("inf")] * len(arr)
        dp[0] = 0
        
        while queue:
            node = queue.popleft()
            
            if node and dp[node - 1] == float("inf"):
                dp[node - 1] = dp[node] + 1
                queue.append(node - 1)
            
            if node < len(arr) - 1 and dp[node + 1] == float("inf"):
                dp[node + 1] = dp[node] + 1
                queue.append(node + 1)
                
            for v in valNodeMap[arr[node]]:
                if dp[v] != float("inf"): continue
                dp[v] = dp[node] + 1
                queue.append(v)
            valNodeMap[arr[node]].clear()
        return dp[-1]
                    
            
            
        
        
        