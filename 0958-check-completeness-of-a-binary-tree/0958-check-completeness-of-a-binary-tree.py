# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        visit = [False] * 101
        
        def dfs(node : TreeNode, code : int):
            if not node: return 
            visit[min(100, code)] |= node != None
        
            dfs(node.left, code * 2 + 1)
            dfs(node.right, code * 2 + 2)
            
        dfs(root, 0)
        
        return not visit[-1] and visit.index(False) > 100 - operator.indexOf(reversed(visit), True) 

        
            
