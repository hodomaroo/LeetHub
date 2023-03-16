# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(postorder[-1])
        
        def dfs(poL : int, poR : int, inL : int, inR : int): #구간은 [left, right]
            if poL == poR: return
            cur = TreeNode(postorder[poR - 1])
                
            
            leftEnd = inorder.index(postorder[poR - 1], inL, inR)
            
            lSize = leftEnd - inL
            rSize = inR - inL - lSize
            
            cur.left, cur.right = dfs(poL, poL + lSize, inL, leftEnd), dfs(poR - rSize , poR - 1, leftEnd + 1, inR)
            return cur
        
        return dfs(0, len(postorder), 0, len(inorder))
            
                
            
            
            
            
            
                
            
        
        