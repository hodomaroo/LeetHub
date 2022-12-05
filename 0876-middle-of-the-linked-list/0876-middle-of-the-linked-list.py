# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node,length = head,0
        
        while node:
            length += 1
            node = node.next
        
        for i in range(length // 2):
            head = head.next
        return head
            