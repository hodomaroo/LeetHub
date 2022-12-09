# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(_min : int,_max : int, node : TreeNode):
            val = max(abs(node.val - _max), abs(node.val - _min))
            
            if node.left:
                val = max(dfs(min(node.val,_min),max(node.val, _max), node.left),val)
            if node.right:
                val = max(dfs(min(node.val,_min),max(node.val, _max), node.right),val)
            return val
        return dfs(root.val,root.val,root)
                
                