class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def Traverse(node : TreeNode):
            if node.left:   Traverse(node.left)
                
            result.append(node.val)
            
            if node.right:  Traverse(node.right)
        Traverse(root)
        return result[k-1]     
    
            
