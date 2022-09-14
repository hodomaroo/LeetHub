# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        stat = 0
        count = 0
        def valid(node : TreeNode):
            
            
            nonlocal stat,count
            stat ^= 1 << node.val
            if node.left:
                valid(node.left)
            if node.right:
                valid(node.right)
                
            if not(node.left or node.right):
                sstat = stat & -stat
                if not (~sstat & stat) or not stat:
                    count += 1
                
            stat ^= 1 << node.val
        
        valid(root)
        
        return count
                
                
                 
        