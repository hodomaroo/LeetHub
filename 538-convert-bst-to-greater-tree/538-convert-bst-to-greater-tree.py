#Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        valueList = []
        
        def CollectValues(node: TreeNode, value: int) -> int:
            #TraverseEveryNode

            if node.right:
                value = CollectValues(node.right, value)

            value += node.val
            valueList.append(value)

            if node.left:
                value = CollectValues(node.left, value)

            return value

        def TraverseAndConvert(node: TreeNode):
            if node.left:
                TraverseAndConvert(node.left)

            node.val = valueList.pop()

            if node.right:
                TraverseAndConvert(node.right)
        
        if not root:   return root
        
        CollectValues(root, 0)
        TraverseAndConvert(root)
        return root
        #value는 애초에 정렬되어있는 상태임


