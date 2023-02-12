class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = [[] for _ in range(len(roads) + 1)]
        
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(par : int, node : int) -> List[int]: #Number of Child / CurrentTotalFuel
            count, fuel = 1,0
            
            for child in graph[node]:
                if child == par: continue
                    
                c,f = dfs(node, child)
                count,fuel = count + c, fuel + f + ceil(c / seats)
                
            return [count, fuel] 
                
        return dfs(-1, 0)[1]
            
            
            
            