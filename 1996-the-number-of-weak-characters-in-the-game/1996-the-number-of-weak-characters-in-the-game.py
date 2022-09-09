class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: x[0])
        properties.sort(key = lambda x: -x[1])
        properties.sort(key = lambda x : (-x[0], x[1]))
        
        maxi = float("-inf")
        count = 0
        
        for att, dep in properties:
            if maxi > dep:
                count += 1
            maxi = max(dep,maxi)
            
        return count
            
        
        