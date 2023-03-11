# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        
        def dfs(left : int, right : int) -> TreeNode: #구간 -> [left, right)
            mid = (left + right) // 2
            if left == right:   return None
            
            node = TreeNode(val = nodes[mid])
            
            node.left, node.right = dfs(left, mid),dfs(mid + 1, right)
            return node
            
        return dfs(0, len(nodes))
            
            