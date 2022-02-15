from collections import Counter
from copy import deepcopy
# Definition for a binary tree node.
"""
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
"""

class Solution(object):
    def pathSum(self, root, targetSum):
        def getTotalCount(cur,counter):
            if not cur: return 0
            ans = 0

            nextCounter = Counter()
            for v in counter:
                nextCounter[v + cur.val] += counter[v]
            nextCounter[cur.val] += 1

            ans += nextCounter[targetSum]

            if cur.left:    ans += getTotalCount(cur.left,nextCounter)
            if cur.right:   ans += getTotalCount(cur.right,nextCounter)

            return ans
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        return getTotalCount(root,Counter())
