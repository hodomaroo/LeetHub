# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        stack = []
        
        while node:
            stack.append(node)
            node = node.next
        
        if n != len(stack):
            stack[-n - 1].next = stack[-n - 1].next.next 
        
        else:      head = head.next
            
        return head
        