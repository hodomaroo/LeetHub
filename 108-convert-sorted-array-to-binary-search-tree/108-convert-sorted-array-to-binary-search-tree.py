# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def devideAndConquer(parent : TreeNode, left : int, right : int) -> int:
            if left == right: return
            
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            
            node.left = devideAndConquer(mid, left, mid)
            node.right = devideAndConquer(mid, mid + 1, right)
            
            return node
        return devideAndConquer(None,0,len(nums))
        