class Solution:
    def concatenatedBinary(self, n: int) -> int:
        cur = 0
        MOD = pow(10,9) + 7
        
        for ii in range(1,n + 1):
            for count in range(20, -1, -1):
                if ii & (1 << count): break
                
            cur = (cur * (2 << count) + ii) % MOD
        return cur     