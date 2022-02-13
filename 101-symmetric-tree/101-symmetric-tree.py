# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):

        def dualTraverse(cur1,cur2):
            if cur1.val != cur2.val: return False

            if (cur1.left and not cur2.right) or (not cur1.left and cur2.right): return False
            if (cur1.right and not cur2.left) or (not cur1.right and cur2.left): return False


            if cur1.left and cur2.right and not dualTraverse(cur1.left,cur2.right): return False
            if cur1.right and cur2.left and not dualTraverse(cur1.right,cur2.left): return False

            return True

        return dualTraverse(root,root)








        """
        :type root: TreeNode
        :rtype: bool
        """
        #왼쪽으로 진행하며 커서 오른쪽으로 변경
        #오른쪽으로 진행하며 커서 왼쪽으로 변경
