class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        #자기 자신도 child로 생각하는게 가능
        childs,sums = [1] * n,[0] * n
        visit = [False] * n
        graph = [[] for _ in range(n)]
        
        def dfs1(node : int):
            if visit[node]: return 
            visit[node] = True
                        
            for nextnode in graph[node]:
                if visit[nextnode]: continue
                
                dfs1(nextnode)
                sums[node] += sums[nextnode] + childs[nextnode]
                childs[node] += childs[nextnode]
        
        def dfs2(node : int):
            if visit[node]: return
            visit[node] = True
        
            for nextnode in graph[node]:
                if visit[nextnode]: continue
                    
                #자식의 sums값 -> 부모의 전체 sums - 해당 자식으로 인해 유래된 값 + (루트의 자식 - 해당 자식의 전체 자식 수)
                sums[nextnode] += sums[node] - (sums[nextnode] + childs[nextnode]) + (childs[node] - childs[nextnode])
                childs[nextnode] = childs[0]
                
                dfs2(nextnode)
                
       
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        dfs1(0)        
        
        visit = [False] * n
        dfs2(0)
    
        return sums
        
        
            
            
            
                
            
            