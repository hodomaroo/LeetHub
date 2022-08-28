class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        
        count = 0
        for v in sorted(s):
            if g and v >= g[-1]:
                count += 1
                g.pop()
        
        return count
                
                
            