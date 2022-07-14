from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        root = TreeNode()

        def DevideAndConquer(node : TreeNode, preIndex : int , left : int, right : int) -> None:
            
            node.val = preorder[preIndex] #
            index = inorder.index(node.val) #val 기준으로 split
            
            
            #index = 2로 되니까 ,  left = 0, right = 1 형태로 형성
            #preIndex -> 1이므로,  index 0 left 0 right 1 
            #preIndex -> 1로 또 들어감/// 
            if left < index:
                node.left = TreeNode()
                DevideAndConquer(node.left, preIndex=preIndex + 1, left=left, right=index - 1)

            #index + 1부터 오른쪽 자식
            if right > index: #오른쪽에 구간이 존재하면         
                node.right = TreeNode()
                DevideAndConquer(node.right, preIndex = preIndex + (index - left) + 1, left=index + 1, right= right)
            
                
        DevideAndConquer(root, preIndex= 0, left= 0, right= len(preorder) - 1)
        return root










