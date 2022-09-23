class Solution:
    def concatenatedBinary(self, n: int) -> int:
        cur = 0
        MOD = pow(10,9) + 7
        
        for i in range(1,n + 1):        
            cur = (cur * (2 << int(log2(i))) + i) % MOD
        return cur     