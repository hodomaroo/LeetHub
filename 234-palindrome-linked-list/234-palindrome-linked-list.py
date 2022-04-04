# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        values = []
        while head:
            values.append(head.val)
            head = head.next
            
        for i in range(len(values) // 2):
            if values[i] != values[-1 - i]: return False
        return True
        