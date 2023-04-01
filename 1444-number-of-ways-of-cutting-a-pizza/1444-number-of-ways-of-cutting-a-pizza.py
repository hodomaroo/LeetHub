class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        prefix = [[vv == 'A' for vv in v] for v in pizza]
        MOD = 10 ** 9 + 7
        for i in range(len(prefix)):
            for j in range(len(prefix[0])):
                if i:   prefix[i][j] += prefix[i - 1][j]
                if j:   prefix[i][j] += prefix[i][j - 1]
                if i and j: prefix[i][j] -= prefix[i - 1][j - 1]
        
        #print(*prefix, sep = "\n")
        
        def getArea(left : int, right : int, low : int, high : int):
            _sum = prefix[high][right]
            
            if left: _sum -= prefix[high][left - 1]
            if low: _sum -= prefix[low - 1][right]
            if low and left: _sum += prefix[low - 1][left - 1]
            return _sum
        
        #print(getArea(1,2,2,2))
        
        @lru_cache(None)
        def cutting(iMost : int, jMost : int, remain : int) -> int:
            #print("   " * (k - 1 - remain), iMost, jMost, remain)
            if not remain: return 1
            
            _ans = 0
            
            for j in range(jMost,len(pizza[0]) - 1): #otherArea[iMost:i] getArea[i + 1, len(pizza)]
                get = getArea(j + 1,len(pizza[0]) - 1, iMost, len(pizza) - 1)
                other = getArea(jMost, j, iMost, len(pizza) - 1)
                
                
                if not other or get < remain: continue
                #print("   " * (k - 1 - remain), iMost, jMost, remain, get,other, "divㅣ", j)
                _ans += cutting(iMost, j + 1, remain - 1)
                
            for i in range(iMost,len(pizza) - 1): #otherArea[iMost:i] getArea[i + 1, len(pizza)]
                get = getArea(jMost,len(pizza[0]) - 1, i + 1, len(pizza) - 1)
                other = getArea(jMost,len(pizza[0]) - 1, iMost, i)
                
                
                if not other or get < remain: continue
                #print("   " * (k - 1 - remain), iMost, jMost, remain, get,other, "divㅡ", i)
                #print("   " * (k - 1 - remain), jMost, len(pizza[0])-1, i + 1, len(pizza) - 1)
                
                _ans += cutting(i + 1, jMost, remain - 1)
            return _ans % MOD
        return cutting(0,0,k - 1)
            
            