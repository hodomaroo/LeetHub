# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(left : int, right : int, node : TreeNode) -> bool:
            if node.val <= left or node.val >= right: 
                return False
            
            if node.left:
                if not dfs(left, node.val, node.left):
                    return False
            
            if node.right:
                if not dfs(node.val, right, node.right):
                    return False
            
            return True
        return dfs(-float("inf"), float("inf"), root)