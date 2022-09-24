class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10** 9 + 7
        dpOfFourLetters = [0] * (pow(10,5) + 1)
        dpOfThreeLetters = [0] * (pow(10,5) + 1)
        dpOfFourLetters[0] = dpOfThreeLetters[0] = 1
        
        def getTopDownDpOfFourLetters(n : int ) -> int: #개수가 n개일 때의 dp값
            if dpOfFourLetters[n]: return dpOfFourLetters[n]
            
            dpOfFourLetters[n] = sum(getTopDownDpOfFourLetters(n - i) for i in range(1,min(n + 1 ,5))) % MOD
            return dpOfFourLetters[n]
        
        def getTopDownDpOfThreeLetters(n : int ) -> int: #개수가 n개일 때의 dp값
            if dpOfThreeLetters[n]: return dpOfThreeLetters[n]
            
            dpOfThreeLetters[n] = sum(getTopDownDpOfThreeLetters(n - i) for i in range(1,min(n + 1,4))) % MOD
            return dpOfThreeLetters[n]
        
        stack = []
        for v in pressedKeys:
            if not stack or stack[-1][0] != v:
                stack.append([v,1])
            else:
                stack[-1][1] += 1
        
        ans = 1
        for v,c in stack:
            ans = ans * (getTopDownDpOfThreeLetters(c) if v not in ("7","9") else getTopDownDpOfFourLetters(c)) % MOD
        
        return ans
            
            
        
        
        
        
        