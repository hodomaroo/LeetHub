# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        length = head != None
        
        _prev = head
        while _prev.next:
            _prev = _prev.next
            length += 1
        
        if length <= 1:
            return True
        
        _prev = head
        for i in range(length // 2 + length % 2):
            if i == (length // 2 + length % 2 - 1):
                sv = _prev.next
                _prev.next = None
                _prev = sv
            else:
                _prev = _prev.next
        
        _next = _prev.next #원래 다음 노드가 가르키던 곳 /
        _prev.next = None
        
        while _next:
            _nnext = _next.next #다다음 노드! -> 세이브 해놓을 필요 있음
            _next.next = _prev #다음 노드의 이전 노드(현재 노드)
            _prev = _next 
            _next = _nnext #다음노드를 _nnext로 변경
        
        while head and _prev:
            if head.val != _prev.val:
                return False
            head = head.next
            _prev = _prev.next
        return True
                
        
        
                  
