class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        visit,MIN = [False] * len(colors), -100000
        visit_2 = [False] * len(colors)
        values = [[MIN] * 26 for _ in range(len(colors))]
        graph = [[] for _ in range(len(colors))]
        INVALID = [MIN] * 26
        
        
        for a,b in edges:
            graph[a].append(b)
        
        def dfs(node : int, group : int) -> list[int]:
            
            if visit[node]:                
                return INVALID if (group == visit[node] and visit_2[node]) else values[node]
            
            visit_2[node] = True
            values[node] = [0] * 26 if not graph[node] else [MIN] * 26
            visit[node] = group
            
            for next_node in graph[node]:            
                next_values = dfs(next_node, group)
                if next_values == INVALID:  return INVALID
                
                for i,v in enumerate(next_values):
                    values[node][i] = max(values[node][i], v)
            
            values[node][ord(colors[node]) - ord('a')] += 1
            
            visit_2[node] = False
            
            return values[node]
        
        _ans = MIN
        for i in range(len(colors)):
            if visit[i]: continue
            result = dfs(i,i + 1)
            if result == INVALID:   return -1
            
            _ans = max(_ans, max(result))
            
        return _ans if _ans >= 0 else -1
                    
                    
                    
            