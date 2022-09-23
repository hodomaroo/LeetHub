class Solution:
    def concatenatedBinary(self, n: int) -> int:
        cur = 0
        MOD = pow(10,9) + 7
        
        for ii in range(1,n + 1):
            i = ii
            for count in range(30):
                i //= 2
                if not i: break
                
            cur = (cur * (2 << count) + ii) % MOD
        return cur
        
        
        