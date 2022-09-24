# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node : TreeNode, val : int) -> int:
            nonlocal ans
            child = [node.left, node.right]
            
            if not node.left and not node.right and val == targetSum:   
                ans.append(path.copy())
                return 
        
            for childnode in child:
                if childnode:
                    path.append(childnode.val)
                    dfs(childnode, val + childnode.val)
                    path.pop()
        if root:
            path = [root.val]
            dfs(root, root.val)
        return ans
            