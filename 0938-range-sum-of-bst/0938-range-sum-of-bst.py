# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(left : int, right : int, node : TreeNode) -> int:
            nonlocal low, high
            val = node.val if low <= node.val <= high else 0
            
            if node.left and low < node.val:
                val += dfs(left, node.val, node.left)
            
            if node.right and high > node.val:
                val += dfs(node.val, right, node.right)
            return val
        return dfs(-float("inf"),float("inf"),root)