# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maximumDepth = 0

    def maxDepth(self, root):
        def traverse(root,depth):
            self.maximumDepth = max(depth,self.maximumDepth)
            if root.left: traverse(root.left,depth+1)
            if root.right: traverse(root.right,depth+1)
        if root:    traverse(root,1)
        return self.maximumDepth