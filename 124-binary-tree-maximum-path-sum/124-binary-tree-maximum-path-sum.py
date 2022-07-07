from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        def dfs(node : TreeNode) -> int:
            l,lMax = dfs(node.left) if node.left else [0,-float("inf")]
            r,rMax = dfs(node.right) if node.right else [0,-float("inf")]

            curVal = node.val + max(0, l, r)
            self.ans = max(self.ans, node.val + l + r, curVal)
            return [curVal, max(curVal, node.val + l + r, lMax, rMax)]

        return dfs(root)[1]




