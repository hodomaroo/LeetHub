class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = defaultdict(list)
        
        def find(node : str) -> list:
            if node not in parent or parent[node][0] == node:
                parent[node] = [node,1]
            
            else:
                #print(parent, parent[node][0])
                parentNode, value = find(parent[node][0])
                parent[node] = [parentNode, parent[node][1] * value]
                
            return parent[node]
            
        
        def union(a : str, b : str, val : int):
            pa, pb = find(a), find(b)
            parent[pa[0]] = [pb[0], pb[1] / pa[1] * val]
        
        for pair, value in zip(equations, values):
            union(pair[0], pair[1], value)
    
        return [-1 if (a not in parent or b not in parent or find(a)[0] != find(b)[0]) else find(a)[1] / find(b)[1] for a,b in queries]
                
            
        
        