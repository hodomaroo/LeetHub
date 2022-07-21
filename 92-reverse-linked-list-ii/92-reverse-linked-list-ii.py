
from typing import Optional,List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        node : ListNode = head

        while node:
            stack.append(node)
            node = node.next

        stack[left-1:right] = stack[left-1: right][::-1]
        
        head = stack[0]
        node = head 
        
        
        for v in stack[1:]:
            node.next = v
            node = node.next
        node.next = None
        return head
            