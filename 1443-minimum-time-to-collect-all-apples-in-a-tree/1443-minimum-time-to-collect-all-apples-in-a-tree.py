class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        visit = [False] * n
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node : int) -> int:
            visit[node] = True
            res = sum(dfs(child) for child in graph[node] if not visit[child])
            print(node, res)
            return res + (hasApple[node] or res > 0) * 2 * (node != 0)
            
            
        return dfs(0)