# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        visit = [False] * 100
        flag = False
        def dfs(node : TreeNode, code : int):
            if not node: return
            if code >= 100: 
                flag = True
                return
                
            visit[code] = True
            dfs(node.left, code * 2 + 1)
            dfs(node.right, code * 2 + 2)
        dfs(root, 0)
        
        return not flag and sum(visit) == sum(visit[:visit.index(False)])

        
            
