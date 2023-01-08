class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def func(stdX : int, stdY : int, x: int, y : int, dx : int, dy : int) -> bool:
            if (stdX, stdY) == (x,y):
                return 1
            
            diffX = x - stdX
            diffY = y - stdY
            
            if diffX % dx: return 0
            mod = diffX // dx
            
            return int(y == (stdY + dy * mod))
        
        _max = 1


        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                v1,v2 = points[i], points[j]
                if v1[0] == v2[0]:
                    #x = p인 그래프
                    _max = max(_max, sum(v[0] == v1[0] for v in points))
            
                elif v1[1] == v2[1]:
                    #y = p인 그래프
                    _max = max(_max, sum(v[1] == v1[1] for v in points))
                
                else:
                    dx,dy = map(sub, v1,v2)
                    dx,dy = map(lambda x : x // gcd(dx,dy), (dx,dy))

                    _max = max(_max, sum(func(v1[0],v1[1], x, y, dx, dy) for x,y in points))
                
                               
        return _max