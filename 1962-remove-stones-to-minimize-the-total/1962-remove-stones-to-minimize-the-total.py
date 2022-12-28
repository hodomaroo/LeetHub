class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-v for v in piles]
        heapify(piles)
        
        while piles[0] and k:
            heappush(piles, piles[0] + abs(heappop(piles)) // 2)
            k -= 1
        
        print(piles)
        return -sum(piles)
            