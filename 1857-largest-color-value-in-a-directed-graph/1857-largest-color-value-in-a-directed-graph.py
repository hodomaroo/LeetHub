class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        visit,MIN = [False] * len(colors), -100000
        visit_2 = [False] * len(colors)
        values = [[MIN] * 26 for _ in range(len(colors))]
        graph = [[] for _ in range(len(colors))]
        INVALID = [MIN] * 26
        cycle_detected = False
        
        
        for a,b in edges:
            graph[a].append(b)
        
        def dfs(node : int, group : int) -> list[int]:
            nonlocal cycle_detected
            
            if visit[node]:
                if visit[node] == group and visit_2[node]:
                    cycle_detected = True
                    
                return INVALID if (group == visit[node] and visit_2[node]) else values[node]
            
            visit_2[node] = True
            values[node] = [0] * 26 if not graph[node] else [MIN] * 26
            visit[node] = group
            
            for next_node in graph[node]:            
                for i,v in enumerate(dfs(next_node, group)):
                    values[node][i] = max(values[node][i], v)
            
            values[node][ord(colors[node]) - ord('a')] += 1
            
            visit_2[node] = False
            
            return INVALID if max(values[node]) < 0 else values[node]
        
        _ans = MIN
        for i in range(len(colors)):
            if visit[i]: continue
            _ans = max(_ans, max(dfs(i,i + 1)))
            if cycle_detected:  return -1
            
        #print(values)
        return _ans if _ans >= 0 else -1
                    
                    
                    
            