class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        powSet = {1}
        v = 1     
        while v < 2 **31:
            powSet.add(v)
            v *= 3
        return n in powSet
            
            
            
            
            
            