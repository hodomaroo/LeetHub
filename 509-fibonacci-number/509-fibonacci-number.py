class Solution:
    
    
    
    def fib(self, n: int) -> int:
        fibs = [-1] * 31
        fibs[0] = 0
        fibs[1] = 1
        
        def fibo(n : int) -> int:
            if fibs[n] != -1:
                return fibs[n]

            fibs[n] = fibo(n - 1) + fibo(n - 2) 
            return fibs[n]
    
    
        return fibo(n)
    
        