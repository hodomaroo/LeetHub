# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        visits = []
        
        def dfs(node : TreeNode, pos : int, depth : int):
            nonlocal visits
            
            visits.append((pos,depth,node.val,))
            
            if node.left:
                dfs(node.left, pos - 1, depth + 1)
            
            if node.right:
                dfs(node.right, pos + 1, depth + 1)
            
        dfs(root, 0, 0)
        
        visits.sort()
        ans = []
        line = []
        nowPos = None
        
        for pos,depth,v in visits:
            if not line or nowPos == pos:
                line.append(v)
                nowPos = pos
            
            else:
                nowPos = pos
                ans.append(line[:])
                line = [v]
        ans.append(line)
        return ans
        