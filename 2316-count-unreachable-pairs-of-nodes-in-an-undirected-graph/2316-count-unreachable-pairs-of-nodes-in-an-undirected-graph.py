class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visit = [False] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def bfs(start : int) -> int:
            q = deque([start])
            visit[start] = True
            count = 1
            while q:
                node = q.popleft()

                for nextnode in graph[node]:
                    if visit[nextnode]: continue
                    visit[nextnode] = True
                    count += 1
                    q.append(nextnode)
            return count

    
        areas = []
        for i in range(n):
            if visit[i]: continue
            areas.append(bfs(i))
        
        print(areas)
        return sum((n - areas[i]) * areas[i] for i in range(len(areas))) // 2
        

