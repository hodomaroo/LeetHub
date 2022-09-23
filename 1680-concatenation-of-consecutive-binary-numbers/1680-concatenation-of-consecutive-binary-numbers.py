class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = pow(10,9) + 7
        cur = 0        
        for i in range(1, n + 1):        
            cur = ((cur << (int(log2(i)) + 1)) + i) % MOD
            
        return cur     