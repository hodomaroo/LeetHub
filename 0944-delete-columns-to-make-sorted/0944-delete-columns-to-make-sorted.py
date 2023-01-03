class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(([st[i] for st in strs] != sorted(st[i] for st in strs)) for i in range(len(strs[0])))