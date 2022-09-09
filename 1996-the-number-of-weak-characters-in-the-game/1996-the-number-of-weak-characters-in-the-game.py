class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (-x[0], x[1]))
        
        maxi = 0
        count = 0
        
        for att, dep in properties:
            count += maxi > dep
            maxi = max(dep,maxi)
            
        return count
            
        
        