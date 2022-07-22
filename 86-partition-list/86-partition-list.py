from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        
        node = head
        left = []
        right = []
        while node:
            if node.val < x:
                left.append(node)
            else:
                right.append(node)
                
            node = node.next
        
        left += right
        head = left[0]
        node : ListNode = head
        for v in left[1:]:
            node.next = v
            node = node.next
        node.next = None
        return head
        