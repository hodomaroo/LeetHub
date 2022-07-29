# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node : TreeNode) -> int:
            values = [0,node.val]
            
            if node.left:
                lmax = dfs(node.left)
                values[0] += max(lmax)
                values[1] += lmax[0]
            
            if node.right:
                rmax = dfs(node.right)
                values[0] += max(rmax)
                values[1] += rmax[0]
            
            
            
            return values
        
        return max(dfs(root)) if root else 0
                
            
            
        