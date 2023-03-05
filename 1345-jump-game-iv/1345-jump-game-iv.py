class Solution:
    def minJumps(self, arr: List[int]) -> int:
        MAX = 100000
        queue = deque([0])
        valNodeMap = defaultdict(list)
        
        for i in range(len(arr)):
            valNodeMap[arr[i]].append(i)
            
        dp = [MAX] * len(arr)
        dp[0] = 0
        
        while queue:
            node = queue.popleft()
            
            for v in [node -1, node + 1]:
                if 0 <= v < len(arr) and dp[v] == MAX:
                    dp[v] = dp[node] + 1
                    queue.append(v)
                
            for v in valNodeMap[arr[node]]:
                if dp[v] != MAX: continue
                dp[v] = dp[node] + 1
                queue.append(v)
                
            valNodeMap[arr[node]] = []
        return dp[-1]
                    
            
            
        
        
        