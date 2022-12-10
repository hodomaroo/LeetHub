# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD,_sum = 10**9 + 7, dict()
        def dfs(node : TreeNode) -> int:
            _sum[node] = node.val + (dfs(node.left) if node.left else 0) + (dfs(node.right) if node.right else 0)
            print(_sum[node])
            return _sum[node]
        dfs(root)
        
        target = min(_sum.values(), key = lambda x : abs(_sum[root] // 2 - x))
        return target * (_sum[root] - target) % MOD
        
        
        
        
        
            