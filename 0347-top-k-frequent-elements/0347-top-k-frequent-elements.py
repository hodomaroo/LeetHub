class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [v[0] for v in sorted(Counter(nums).items(), key = lambda x : -x[1])][:k]