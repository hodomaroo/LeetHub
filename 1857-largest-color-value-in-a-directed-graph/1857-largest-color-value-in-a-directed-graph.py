class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        groups,MIN = [False] * len(colors), -100000
        visit = [False] * len(colors)
        values = [[MIN] * 26 for _ in range(len(colors))]
        graph = [[] for _ in range(len(colors))]
        
        INVALID = [MIN] * 26
        
        for a,b in edges:
            graph[a].append(b)
        
        def dfs(node : int, group : int) -> list[int]:
            
            if groups[node]:                
                return INVALID if (group == groups[node] and visit[node]) else values[node]
            
            visit[node] = True
            values[node] = [0] * 26 if not graph[node] else [MIN] * 26
            groups[node] = group
            
            for next_node in graph[node]:            
                next_values = dfs(next_node, group)
                if next_values == INVALID:  return INVALID
                
                for i,v in enumerate(next_values):
                    values[node][i] = max(values[node][i], v)
            
            values[node][ord(colors[node]) - ord('a')] += 1
            visit[node] = False
            
            return values[node]
        
        _ans = MIN
        
        for i in range(len(colors)):
            if groups[i]: continue
            result = dfs(i,i + 1)
            if result == INVALID:   return -1
            
            _ans = max(_ans, max(result))
            
        return _ans if _ans >= 0 else -1
                    
                    
                    
            