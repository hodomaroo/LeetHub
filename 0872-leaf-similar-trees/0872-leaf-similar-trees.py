class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node : TreeNode):
            if not node.left and not node.right:
                return [node.val]
            
            return (dfs(node.left) if node.left else []) + (dfs(node.right) if node.right else [])
        
        return dfs(root1) == dfs(root2)