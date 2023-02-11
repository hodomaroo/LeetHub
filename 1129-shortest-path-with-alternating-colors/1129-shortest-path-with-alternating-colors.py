class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        dp = [[float("inf"),float("inf")] for _ in range(n)]
        dp[0] = [0,0]
        q = deque([(0,False), (0,True)]) #node / idx
        
        graph = [[[] for _ in range(n)] for _ in range(2)]
        
        for a,b in redEdges:
            graph[0][a].append(b)
        
        for a,b in blueEdges:
            graph[1][a].append(b)
            
        while q:
            node,boolean = q.popleft()
            
            for next_node in graph[not boolean][node]:
                if dp[next_node][not boolean] != float("inf"): continue
                
                dp[next_node][not boolean] = dp[node][boolean] + 1
                q.append((next_node, not boolean))
                
        return [min(dp[i]) if min(dp[i]) != float("inf") else -1 for i in range(n)]
    
                    
                    
            
            
                
            
            
        
        