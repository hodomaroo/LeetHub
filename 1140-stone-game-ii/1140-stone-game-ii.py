class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        prefix = list(accumulate(piles))
        
        #현재 자기가 만들 수 있는 가장큰 값을 반환 -> 근데, 어차피 자기가 제일 커질 수 있는 값을 구하는거임 / 굳이 필요 없다!
        #어차피 플레이어가 누구든, 만들 수 있는 값은 동일!
        
        print(prefix)
        @lru_cache(None)
        def dfs(idx : int, m : int) -> int:

            if idx >= len(prefix):  return 0
            return prefix[-1] - (prefix[idx - 1] if idx else 0) - min(dfs(i + 1, max(i - idx + 1, m)) for i in range(idx, min(idx + m * 2, len(prefix)))) #내가 만들 수 있는 제일 큰 합
    
        return dfs(0, 1)
            