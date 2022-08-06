class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        for i in range(1000):
            if (minutesToTest // minutesToDie + 1) ** i >= buckets:
                return i