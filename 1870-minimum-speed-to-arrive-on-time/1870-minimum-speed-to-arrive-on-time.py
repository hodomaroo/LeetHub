class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def judge(speed : int):
            return sum(dist[i] // speed + (dist[i] % speed > 0) for i in range(len(dist) - 1)) + dist[-1] / speed
        
        left, right = 0, pow(10,7) + 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if judge(mid) > hour:
                left = mid
            else:
                right = mid
        
        print(left, right)
        return right if judge(right) <= hour else -1
            
            
            