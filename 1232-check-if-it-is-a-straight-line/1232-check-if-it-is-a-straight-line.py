class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        return len(set([(c[i][1] - c[i + 1][1]) / (c[i][0] - c[i + 1][0]) if c[i][0] != c[i+1][0] else -1 for i in range(len(c) - 1)])) == 1