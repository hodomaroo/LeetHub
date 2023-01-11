class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph,visit = [[] for _ in range(n)], [False] * n
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node : int) -> int:
            visit[node] = True
            res = sum(dfs(child) for child in graph[node] if not visit[child])
            return res +  (0 if node == 0 else (hasApple[node] or res > 0) * 2)
            
            
        return dfs(0)