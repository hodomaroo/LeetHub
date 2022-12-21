class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visit = [0] * n
        graph = [[] for _ in range(n)]
        
        for a,b in dislikes:
            graph[a - 1].append(b-1)
            graph[b - 1].append(a-1)
        
        #0 not visited
        #1 a group
        #2 b group
        
        
                
        for node in range(n):
            if visit[node]: continue
            queue = deque([node])        
            
            visit[node] = 1
            while queue:
                node = queue.popleft()
                
                for next_node in graph[node]:
                    if visit[next_node] == visit[node]:
                        return False
                    if not visit[next_node]:
                        visit[next_node] = 1 if visit[node] == 2 else 2
                        queue.append(next_node)
        return True
                    
                    
            
                
            
            
                
            
            
            
            
        