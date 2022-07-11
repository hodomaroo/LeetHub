from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node : TreeNode, depth : int):
            if len(ans) == depth:
                ans.append(node.val)
            
            if node.right:
                dfs(node.right,depth + 1)
            if node.left:
                dfs(node.left,depth + 1)
        if root:
            dfs(root,0)
        
        return ans
            