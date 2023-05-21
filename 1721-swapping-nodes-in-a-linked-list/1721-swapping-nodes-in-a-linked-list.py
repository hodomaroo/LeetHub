# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack, node = [], head
        
        while node:
            stack.append(node)
            node = node.next
            
        if k > len(stack) // 2:
            k = len(stack) - k + 1
        
        a,b = stack[k - 1], stack[-k]
    
        a.next,b.next = b.next, a.next
    
            
        
        
        if k != len(stack) // 2 or len(stack) % 2:
            if k > 1:
                stack[k - 2].next = b
            else:
                head = b
                
            if k != len(stack):
                stack[-k - 1].next = a
        
        
        else:
            b.next = a
            if k > 1:
                stack[k - 2].next = b
            else:
                head = b
    
        return head
            
            
        

[7,9,6,6,7,8,3,0,9,5]
[7,9,6,6,8,7,3,0,9,5]