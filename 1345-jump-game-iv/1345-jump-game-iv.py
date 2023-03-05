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
            
            for v in [node - 1, node + 1] + valNodeMap[arr[node]]:
                if 0 <= v  and v < len(arr) and dp[v] == MAX:
                    queue.append(v)
                    dp[v] = dp[node] + 1
                
            valNodeMap[arr[node]] = []
        return dp[-1]
                    
            
            
        
        
        