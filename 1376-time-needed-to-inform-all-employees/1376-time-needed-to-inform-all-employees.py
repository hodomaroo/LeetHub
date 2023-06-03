class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        for i,v in enumerate(manager):
            if v < 0: continue
            graph[v].append(i)
            indegree[i] += 1
        
        def dfs(node : int) -> int:
            return max(dfs(next_node) for next_node in graph[node]) + informTime[node] if graph[node] else 0
        
        return max(dfs(i) for i in range(n) if not indegree[i])
                
        
        
        
        
        
        
        