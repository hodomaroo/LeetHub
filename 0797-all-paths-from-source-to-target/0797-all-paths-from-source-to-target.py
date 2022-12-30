class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def dfs(node : int, stat : int, route : list[int]):
            nonlocal ans, graph
    
            if node == len(graph) - 1:
                ans.append(route[:])
                return
            
            for nextNode in graph[node]:
                route.append(nextNode)
                dfs(nextNode, stat | (1 << node), route)
                route.pop() 
                
        dfs(0, 1, [0])
        return ans
                
            
                
            
            